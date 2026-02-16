import cv2 
import random
from ultralytics import YOLO
# from google.colab.patches import cv2_imshow # ini ga ketemu pake yang mana

# yolo = YOLO('model/yolov8s.pt') # yolo v8s
yolo = YOLO('model/yolov8n.pt') # yolo v8n

def getColours(cls_num) :
    """ generate unique colors for each class ID """
    random.seed(cls_num)
    return tuple(random.randint(0,255) for _ in range(3))

# load the video
video_path = "yolo/sample.mp4"
videoCap = cv2.VideoCapture(video_path)

# print(videoCap.isOpened())

# procceess video and detect object 
frame_count = 0

win_name = "Yolo detect with video"

# while cv2.waitKey(1) != 27 : # Escape
# while True : 
while videoCap.isOpened() : 
    ret, frame = videoCap.read()
    if not ret : 
        break # break the loop if no frame is read
    
    print(frame)
    # break
    
    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    
    results = yolo.track(frame, stream=True)
    # print (results)
    # break
    
    for result in results :
        class_names = result.names
        
        for box in result.boxes :
            if box.conf[0] > 0.4 :
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                cls = int(box.cls[0])
                class_name = class_names[cls]
                
                conf = float(box.conf[0])
                
                colour = getColours(cls)
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)
                
                cv2.putText(frame, f"{class_name} {conf:.2f}", 
                            (x1, max(y1 - 10, 29)), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.6, colour, 2 )
                
    cv2.imshow(win_name, frame)        
            
    # if frame_count < 20 :
    #     # cv2_imshow(frame)
    #     cv2.imshow(win_name, frame)
    # else :
    #     break
    
    frame_count += 1
    
videoCap.release()
cv2.destroyAllWindows()