import os
import torch
from torchmetrics import JaccardIndex, Dice
import torch.nn as nn
from torch.utils.data import DataLoader
from torch import optim
from tqdm import tqdm

import config
from src.data.utils import CustomDataset
from src.features.utils import get_train_transforms, get_val_transforms
from src.models.model import UNet
from src.visualization.utils import plot_losses

def create_model(n_channels_in: int = 3, n_classes: int = 1):
    model = UNet(n_channels_in,n_classes)
    return model


def check_accuracy(loader, model):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    num_correct = 0
    num_pixels = 0
    dice_metric = Dice(num_classes=2, reduction='sum').to(device)  # Erstellt eine Dice-Instanz
    jaccard_metric = JaccardIndex(num_classes=2, reduction='sum').to(device)  # Erstellt eine JaccardIndex-Instanz
    
    #Eval Mode
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device)
            y = y.to(device).unsqueeze(1)
            preds = torch.sigmoid(model(x))
            preds = (preds > config.THRESHOLD).float()
            num_correct += (preds == y).sum()
            num_pixels += torch.numel(preds)

            # Aktualisiere Dice und Jaccard Metriken
            dice_metric(preds.int(), y.int())  # Achtung: y sollte als Integer vorliegen
            jaccard_metric(preds.int(), y.int())

    # Berechne die endgültigen Metrikwerte
    final_dice = dice_metric.compute()
    final_jaccard = jaccard_metric.compute()

    # Drucke die Metrikwerte
    print(f'Accuracy: {num_correct / num_pixels * 100:.2f}%')
    print(f'Dice Score: {final_dice:.4f}')
    print(f'Jaccard Index: {final_jaccard:.4f}')

    # Zurücksetzen der Metriken für die nächste Verwendung
    dice_metric.reset()
    jaccard_metric.reset()

    #Train Mode
    model.train()



def train_model(
        model,
        train_set = None,
        val_set = None,
        epochs: int = config.NUM_EPOCHS,
        batch_size: int = config.BATCH_SIZE,
        learning_rate: float = config.LEARNING_RATE,
        #load_model: bool = config.LOAD_MODEL,
        num_workers: bool = config.NUM_WORKERS,
        save_checkpoint: bool = config.SAVE_CHECKPOINT,
        gradient_clipping: float = 1.0,
        name: str = config.NAME
    ):

    #Device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    #Create Datasets
    if train_set is None:
        train_set = CustomDataset(config.TRAIN_IMG_DIR, config.TRAIN_MASK_DIR, get_train_transforms())
    if val_set is None:
        val_set = CustomDataset(config.VAL_IMG_DIR, config.VAL_MASK_DIR, get_val_transforms())

    #Create Data Loaders
    train_loader = DataLoader(train_set, shuffle=True, batch_size=batch_size, num_workers=num_workers)
    val_loader = DataLoader(val_set, shuffle=False, drop_last=True, batch_size=batch_size, num_workers=num_workers)

    #Setup the Optimizer, Scheduler, Scaler and Loss Function
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
    grad_scaler = torch.cuda.amp.GradScaler()
    criterion = nn.BCEWithLogitsLoss()
    #global_step = 0


    best_val_loss = float('inf')
    train_losses = []
    val_losses = []

    #Traning Process
    for epoch in range(1, epochs + 1):
        model.train()
        epoch_loss = 0

        with tqdm(total=len(train_set), desc=f'Epoch {epoch}/{epochs}', unit='img') as pbar:
            for batch in train_loader:
                images, true_masks = batch 
                images = images.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
                true_masks = true_masks.to(device=device, dtype=torch.long)

                with torch.autocast(device.type if device.type != 'mps' else 'cpu', enabled=False):
                    masks_pred = model(images)
                    loss = criterion(masks_pred.squeeze(1), true_masks.float())

                optimizer.zero_grad()
                grad_scaler.scale(loss).backward()
                grad_scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(), gradient_clipping)
                grad_scaler.step(optimizer)
                grad_scaler.update()

                pbar.update(images.shape[0])
                #global_step += 1
                epoch_loss += loss.item()
                pbar.set_postfix(**{'Epoch loss': epoch_loss})
        

        train_loss = epoch_loss / len(train_loader)
        train_losses.append(train_loss)

        # Update des Schedulers nach jeder Epoche
        scheduler.step()              

        # Validation und Best Model speichern
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for val_batch in val_loader:
                val_images, val_true_masks = val_batch
                val_images = val_images.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
                val_true_masks = val_true_masks.to(device=device, dtype=torch.long)

                val_masks_pred = model(val_images)
                val_loss += criterion(val_masks_pred.squeeze(1), val_true_masks.float()).item()
        
        val_loss /= len(val_loader)
        val_losses.append(val_loss)

        if save_checkpoint:
            # Save the last model
            save_model(model.state_dict(), os.path.join(config.MODEL_DIR, 'trained_models', 'latest_model.pth'))

            # Save the best model
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                save_model(model.state_dict(), os.path.join(config.MODEL_DIR, 'trained_models', 'best_model.pth'))

        print(f'Epoch {epoch} completed. Training loss: {train_loss}. Validation loss: {val_loss}')

    plot_losses(train_losses, val_losses)



def save_model(state, filename='checkpoint.pth'):
    print('Saving checkpoint ...')
    torch.save(state, filename)



def load_model(checkpoint, model):
    print('Loading checkpoint ...')
    model.load_state_dict(torch.load(checkpoint, map_location=device))


def model_inference(checkpoint, data_set):
    # Modell instanziieren
    model = create_model()
    
    # Modell auf das richtige Gerät verschieben
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
        
    # Checkpoint laden
    model.load_state_dict(torch.load(checkpoint, map_location=device))
    model.eval()  # Modell in den Evaluierungsmodus versetzen

    predictions = []

    #Daten laden
    data_loader = DataLoader(data_set, shuffle=False, drop_last=True, batch_size=1, num_workers=config.NUM_WORKERS)

    with torch.no_grad():
        for batch in data_loader:
            images, true_masks = batch
            images = images.to(device=device, dtype=torch.float32, memory_format=torch.channels_last)
            true_masks = true_masks.to(device=device, dtype=torch.long)
            with torch.autocast(device.type if device.type != 'mps' else 'cpu', enabled=False):
                masks_pred = model(images)
                
            predictions.append(masks_pred.cpu())

    return predictions



if __name__ == "__main__":
    #Model Creation
    model = create_model()
    
    #Model Training
    train_model(model)

    #history plots
    print('Train Loss:')
    check_accuracy(model.train_loader, model)
    
    print('Val Loss:')
    check_accuracy(model.val_loader, model)