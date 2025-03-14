import os
import random

import requests
import cv2

from dotenv import load_dotenv
from constants import (URL, CLASS, CLASS_ID,
                       TRAINING, VALIDATION, TESTING,
                       TRAINING_IMAGES_DIR, TRAINING_LABELS_DIR,
                       VALIDATION_IMAGES_DIR, VALIDATION_LABELS_DIR,
                       TESTING_IMAGES_DIR, TESTING_LABELS_DIR,
                       BASE_DIR, RESULTS_DIR)

load_dotenv()

# secrets
KEY = os.getenv('KEY')


def get_image_urls(num: int) -> list:
    try:
        print('Getting urls...')
        resp = requests.get(
            url=URL,
            params={
                'query': CLASS,
                'per_page': num
            },
            headers={'Authorization': KEY}
        )
        data = resp.json()
        print('Urls obtained successfully')
        return [img['src']['original'] for img in data['photos']]
    except Exception as e:
        print(f'Error during request: {e}')


def download_images(url: str, download_dir: str):
    try:
        print(f'Downloading image: {url}')
        resp = requests.get(url)
        with open(download_dir, 'wb') as f:
            f.write(resp.content)
            print(f"Image downloaded successfully: {download_dir}")
    except Exception as e:
        print(f"Error downloading image: {url} - {e}")


def create_annotation(image_path: str, __type: str, download_dir: str):
    print('Creating annotation...')

    image = cv2.imread(image_path)
    height, width, _ = image.shape

    x_center = width / 2 / width
    y_center = height / 2 / height
    box_width, box_height = 0.5, 0.5

    annotation_path = os.path.join(download_dir, os.path.basename(image_path).replace(f'.{__type}', '.txt'))
    with open(annotation_path, 'w') as f:
        f.write(f'{CLASS_ID} {x_center} {y_center} {box_width} {box_height}')
    print(f'Annotation created {annotation_path}')


def create_dir():
    os.makedirs(TRAINING_IMAGES_DIR, exist_ok=True)
    os.makedirs(TRAINING_LABELS_DIR, exist_ok=True)
    os.makedirs(VALIDATION_IMAGES_DIR, exist_ok=True)
    os.makedirs(VALIDATION_LABELS_DIR, exist_ok=True)
    os.makedirs(TESTING_IMAGES_DIR, exist_ok=True)
    os.makedirs(TESTING_LABELS_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)


def save_data(image_urls: list):
    print('Saving data...')

    random.shuffle(image_urls)

    training_perc = int(0.7 * len(image_urls))
    validation_perc = len(image_urls) - int(0.15 * len(image_urls))

    create_dir()

    training_image_paths = []
    validation_image_paths = []
    testing_image_path = []

    for i, url in enumerate(image_urls):
        extension = url.split('.')[-1]
        if i < training_perc:
            images_dir = TRAINING_IMAGES_DIR
            labels_dir = TRAINING_LABELS_DIR
            training_image_paths.append(os.path.join(images_dir, f'image_{i+1}.{extension}'))
        elif training_perc <= i < validation_perc:
            images_dir = VALIDATION_IMAGES_DIR
            labels_dir = VALIDATION_LABELS_DIR
            validation_image_paths.append(os.path.join(images_dir, f'image_{i+1}.{extension}'))
        else:
            images_dir = TESTING_IMAGES_DIR
            labels_dir = TESTING_LABELS_DIR
            testing_image_path.append((os.path.join(images_dir, f'image_{i+1}.{extension}')))

        image_name = os.path.join(images_dir, f'image_{i+1}.jpeg')
        download_images(url=url, download_dir=image_name)

        create_annotation(image_path=image_name, __type=extension, download_dir=labels_dir)

        write_paths(paths=training_image_paths, file=TRAINING)
        write_paths(paths=validation_image_paths, file=VALIDATION)
        write_paths(paths=testing_image_path, file=TESTING)


def write_paths(paths: str, file: str):
    with open(os.path.join(BASE_DIR, f'{file}.txt'), 'w') as f:
        for path in paths:
            f.write(f'{path}\n')
