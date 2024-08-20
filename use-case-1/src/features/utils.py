import albumentations as A
from albumentations.pytorch import ToTensorV2
import config

def get_train_transforms():
    """Erstellt und gibt die Transformationen für den Trainingsdatensatz zurück."""
    train_transform = A.Compose([
        A.Resize(height=config.IMAGE_HEIGHT, width=config.IMAGE_WIDTH),
        A.Rotate(limit=35, p=1.0),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.1),
        A.Normalize(
            mean=[0.485, 0.456, 0.406],  
            std=[0.229, 0.224, 0.225],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ])
    return train_transform

def get_val_transforms():
    """Erstellt und gibt die Transformationen für den Validierungsdatensatz zurück."""
    val_transform = A.Compose([
        A.Resize(height=config.IMAGE_HEIGHT, width=config.IMAGE_WIDTH),
        A.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ])
    return val_transform
