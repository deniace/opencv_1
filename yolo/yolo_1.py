# dari sini https://medium.com/@tejasdalvi927/object-detection-with-yolo-and-opencv-a-practical-guide-cf7773481d11

import cv2
import random
from ultralytics import YOLO
import cvzone
import math

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# model = YOLO('yolo/yolov8n.pt')
model = YOLO('model/20861.pt')

win_name = "OpenCV with Yolo"

while cv2.waitKey(1) != 27 : # Escape :
    success, img = cap.read()
    result = model(img, stream=True)
    
    for r in result :
        
        class_names = r.names
        # print(class_names)    
        # break
        
        boxes = r.boxes
        # print(boxes)
        for box in boxes :
            print("boxes")
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            
            cvzone.cornerRect(img, (x1,y1, w, h))
            
            conf = math.ceil((box.conf[0]*100))/100
            
            cls = box.cls[0]
            # name = classNames[int(cls)]
            name = class_names[int(cls)]
            # print(int(cls))
             
            cvzone.putTextRect(img, f'{name}' f' ({conf})', (max(0, x1), max(35, y1)), scale=1, thickness=1)
            
        cv2.imshow(win_name, img)

cv2.destroyWindow(win_name)