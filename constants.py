import os

# endpoint of the pexels api
URL = 'https://api.pexels.com/v1/search'
NUM = 20
CLASS = 'surgery equipment'

# phases and directories
BASE_DIR = 'dataset'

TRAINING = 'training'
VALIDATION = 'validation'
TESTING = 'testing'
RESULTS = 'results'
TRAINING_DIR = os.path.join(BASE_DIR, TRAINING)
VALIDATION_DIR = os.path.join(BASE_DIR, VALIDATION)
TESTING_DIR = os.path.join(BASE_DIR, TESTING)
RESULTS_DIR = os.path.join(BASE_DIR, RESULTS)

TRAINING_IMAGES_DIR = os.path.join(TRAINING_DIR, 'images')
TRAINING_LABELS_DIR = os.path.join(TRAINING_DIR, 'labels')
VALIDATION_IMAGES_DIR = os.path.join(VALIDATION_DIR, 'images')
VALIDATION_LABELS_DIR = os.path.join(VALIDATION_DIR, 'labels')
TESTING_IMAGES_DIR = os.path.join(TESTING_DIR, 'images')
TESTING_LABELS_DIR = os.path.join(TESTING_DIR, 'labels')

CLASS_ID = 0

# model version
MODEL_VERSION = 'yolo11x.pt'
