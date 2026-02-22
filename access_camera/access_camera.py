import cv2
import sys

# 0 = Default kamera
# 1 = kamera 1
s = 0
print(len(sys.argv))

if len(sys.argv) > 1 :
    s = sys.argv[1]
    print(s)

source = cv2.VideoCapture(s)
print(source)

win_name = 'Camera Preview CV2'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27 : # Escape
    has_frame, frame = source.read()
    if not has_frame :
        break

    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)