import cv2 as cv

img = cv.imread("Before.png")

cv.imshow("Display Window", img)
k= cv.waitKey(0) #wait for a keystroke in the window