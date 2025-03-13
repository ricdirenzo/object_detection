import os
import cv2
from ultralytics import YOLO

from constants import MODEL_VERSION


def predict(chosen_model, img, classes: list, conf=0.5):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)

    return results


def predict_and_detect(chosen_model, img, classes: list, conf=0.5, rectangle_thickness=3, text_thickness=2):
    results = predict(chosen_model, img, classes, conf=conf)
    for result in results:
        for box in result.boxes:
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), rectangle_thickness)
            cv2.putText(img, f"{result.names[int(box.cls[0])]}",
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), text_thickness)
    return img, results


def object_detecting(source_path: str, dest_path: str):
    with open(source_path+'.txt', 'r') as f:
        paths = [row.strip() for row in f.readlines()]

    # model version
    print('Importing model...')
    model = YOLO(MODEL_VERSION)
    print(f'{MODEL_VERSION} imported successfully')

    for path in paths:
        _, file = os.path.split(path)
        print('Reading images...')
        image = cv2.imread(path)
        result_img, _ = predict_and_detect(chosen_model=model, img=image, classes=[], conf=0.5)

        print('Writing result images...')
        cv2.imwrite(os.path.join(dest_path, file), result_img)
        cv2.waitKey(0)
