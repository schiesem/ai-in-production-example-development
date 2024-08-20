#Data
DATASET_DIR = "./../data/"

TRAIN_DIR = DATASET_DIR + "raw/train/"
TRAIN_IMG_DIR = TRAIN_DIR + "imgs/"
TRAIN_MASK_DIR = TRAIN_DIR + "masks/"

VAL_DIR = DATASET_DIR + "raw/val/"
VAL_IMG_DIR = VAL_DIR + "imgs/"
VAL_MASK_DIR = VAL_DIR + "masks/"

TEST_DIR = DATASET_DIR + "raw/test/"
TEST_IMG_DIR = TEST_DIR + "imgs/"
TEST_MASK_DIR = TEST_DIR + "masks/"

#Model
MODEL_DIR = "./../models/"
NAME = "UNet"

#Model Training
LEARNING_RATE = 1e-4
BATCH_SIZE = 4
NUM_EPOCHS = 15
NUM_WORKERS = 4
IMAGE_HEIGHT = 320
IMAGE_WIDTH = 480
LOAD_MODEL = False
SAVE_CHECKPOINT = True

#Model Inference
THRESHOLD = 0.5

#Repots
FIG_DIR = "../reports/figures/"