import ultralytics
from ultralytics import YOLO

print(f"using Ultralytics v {ultralytics.__version__}")

# model = YOLO("yolov8n.yaml") # build a new model from YAML
# model = YOLO("yolov8n.yaml").load("yolov8n.pt") # build from YAML and transfer weights
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

model.train(data = "conf.yaml", epochs = 10)