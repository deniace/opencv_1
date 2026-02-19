from ultralytics import YOLO

model = YOLO("model/best.pt")

# result = model("yolo/0110.jpg")
result = model("yolo/0072.jpg")

result[0].show()