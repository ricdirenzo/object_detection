import os

# constants
URL = 'https://api.pexels.com/v1/search'
NUM = 20
CLASS = 'surgery equipment'

BASE_DIR = 'dataset'
TRAIN_DIR = os.path.join(BASE_DIR, 'train')
VAL_DIR = os.path.join(BASE_DIR, 'val')

# sottocartelle per immagini e annotazioni
TRAIN_IMAGES_DIR = os.path.join(TRAIN_DIR, 'images')
TRAIN_LABELS_DIR = os.path.join(TRAIN_DIR, 'labels')
VAL_IMAGES_DIR = os.path.join(VAL_DIR, 'images')
VAL_LABELS_DIR = os.path.join(VAL_DIR, 'labels')

CLASS_ID = 0