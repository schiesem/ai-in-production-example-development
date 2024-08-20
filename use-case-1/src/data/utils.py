import os
import config
import pickle
from PIL import Image
import numpy as np
import random  
import matplotlib.pyplot as plt
from torch.utils.data import Dataset


#Create Dataset
class CustomDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_filename = self.images[idx]
        img_path = os.path.join(self.image_dir, img_filename)
        mask_path = os.path.join(self.mask_dir, img_filename.replace('.jpg', '.gif'))  
        
        image = Image.open(img_path)
        if image.mode == 'L': #Wenn Bild ein Graustufenbild ist
            image = np.array(image.convert('RGB'))
        else: #Wenn Bild bereits ein RGB-Bild ist  
            image = np.array(image)
            
        mask = np.array(Image.open(mask_path).convert('L'), dtype=np.float32)
        mask[mask == 255.0] = 1.0 #Falls Masks nicht als 0-1 sondern als 0-255 gespeichert sind

        if self.transform is not None:
            augmentations = self.transform(image=image, mask=mask)
            image = augmentations['image']
            mask = augmentations['mask']

        return image, mask


def save_dataset(dataset, file_name):
    with open(config.DATASET_DIR + '/processed/' + file_name + "_metadata", 'wb') as f:
        pickle.dump((dataset.image_dir, dataset.mask_dir, dataset.transform, dataset.images), f)
    with open(config.DATASET_DIR + '/processed/' + file_name, 'wb') as f:
        pickle.dump(dataset, f)


def load_dataset(file_name):
    with open(config.DATASET_DIR + '/processed/' + file_name, 'rb') as f:
    #    image_dir, mask_dir, transform, images = pickle.load(f)
    #return CustomDataset(image_dir, mask_dir, transform, images)
        dataset = pickle.load(f)
        return dataset
    
def plot_random_samples(dataset, num_samples=4):
    fig, axes = plt.subplots(num_samples, 2, figsize=(10, 10))
    fig.suptitle('Random Samples from Dataset', fontsize=16)

    indices = random.sample(range(len(dataset)), num_samples)
    for i, idx in enumerate(indices):
        image, mask = dataset[idx]

        # Transponieren der Bilddaten für matplotlib
        if len(image.shape) == 3:  # Farbige Bilder
            image = np.transpose(image, (1, 2, 0))
        
        axes[i, 0].imshow(image)
        axes[i, 0].set_title(f"Image {idx}")
        axes[i, 0].axis('off')

        axes[i, 1].imshow(mask, cmap='gray')
        axes[i, 1].set_title(f"Mask {idx}")
        axes[i, 1].axis('off')

    plt.tight_layout()
    plt.show()