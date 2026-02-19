import cv2
from ultralytics import YOLO

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(1)
webcam.set(3, 1280)
webcam.set(4, 720)

check, frame = webcam.read()
# cv2.imwrite(filename="yolo/saved_1.jpg", img=frame)
webcam.release() 

# model = YOLO("model/yolov8n.pt")
model = YOLO("model/20861.pt")

result = model.predict(frame, save=True, project="yolo", name="yolo")
cv2.imwrite(filename="yolo/saved_1.jpg", img=result[0])

result[0].show()
