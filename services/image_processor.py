import cv2
import torch

# Завантаження моделі YOLO при імпорті
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Cannot load image: {image_path}")
    
    results = model(img)
    detections = results.pandas().xyxy[0].to_dict(orient="records")
    return detections
