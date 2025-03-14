# Object detection with YOLOv11

#### Data preprocessing
The `preprocessor` script prepare the dataset automatically for an image classification or object detection task. It downloads images from an API, saves them into structured directories (splitted in traning, validation and testing), creates YOLO-format annotations, and organizes image paths into text files for learning.

#### Detecting
The `predictor` and `detector` script uses the YOLOv11 model to perform object detection on images. It loads a 
pre-trained YOLO model, detects objects in images, and saves the processed images with bounding boxes and class labels.
 
