import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

#matplotlib inline

def download_and_unzip(url, save_path) :
    print(f"Downloading and extracting assets....", end="")

    #downloading zip file using using the zipfile package
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package
        with ZipFile(save_path) as z :
            # extract zip file content in the same directory
            z.extractall(os.path.split(save_path)[0])
        print("DONE")
    except:
        print("\nInvalid file. ", e)

URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB1.zip")

# Download if assets zip does not exixt
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

# display 18x18 pixel image
Image(filename="checkerboard_18x18.png")

# display 84x84 pixel image
Image(filename="checkerboard_84x84.jpg")

# read image as gray scale
cb_img = cv2.imread("checkerboard_18x18.png",0)

# print the image data (pixel value), element of a 2D numpy array
# each pixel value is 8bit [0,255]
print(cb_img)

# print the size of image
print("Image size (H, W) is : ", cb_img.shape)

# print data type of image
print("Data type image is : ", cb_img.dtype)

# Display image using matplotlib
plt.imshow(cb_img)
# plt.show()

# set color map to gray scale for proper rendering
plt.imshow(cb_img, cmap="gray")
# plt.show()


# read image as gray scale
cb_img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)

# print image
print(cb_img_fuzzy)

# display image
plt.imshow(cb_img_fuzzy, cmap="gray")
# plt.show()

print("last")
# read and display coca-cola logo
Image(filename="coca-cola-logo.png") # ini masih ga ke display image nya

# read image
coke_img = cv2.imread("coca-cola-logo.png", 1)

# print the size of image
print("Image size (H, W, C) is : ", coke_img.shape)

# print datatype of image
print("Data type of image", coke_img.dtype)

plt.imshow(coke_img)
# plt.show()  

coke_img_channel_reserved = coke_img[:,:,::-1]

plt.imshow(coke_img_channel_reserved)
# plt.show()

# Spliting and merging color
# cv2.split() # Divides multichanel array  into several single-channel array
# cv2.merge() # Merges seceral arrays to make a single multi-channel array, All the input matrix must have same size

# plit the image into the B, G, R element
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

b, g, r = cv2.split(img_NZ_bgr)

# show the channel 
plt.figure(figsize=[15, 4])
# plt.show()

plt.subplot(141); plt.imshow(r, cmap="gray"); plt.title("Red channel")
plt.subplot(142); plt.imshow(g, cmap="gray"); plt.title("green channel")
plt.subplot(143); plt.imshow(b, cmap="gray"); plt.title("blue channel")

# merge the individual channel into a BGR image
imgMerged = cv2.merge((b, g, r))

# show the merged output
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged output")
plt.show()

# print("asdf")
# Opencv stores color channel in a difference order than the most other application (BGR vs RGB)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
# print(img_NZ_rgb)
plt.imshow(img_NZ_rgb)
plt.title("RGB Channel")
plt.show()

# changing to HSV Color Space
img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

# Split image to the B, G, R Component
h,s,v = cv2.split(img_hsv)

# shww the channels
plt.figure(figsize=[15,4])
plt.subplot(141); plt.imshow(h, cmap="gray"); plt.title("H Channel")
plt.subplot(142); plt.imshow(s, cmap="gray"); plt.title("S Channel")
plt.subplot(143); plt.imshow(v, cmap="gray"); plt.title("V Channel")
plt.subplot(144); plt.imshow(img_NZ_rgb); plt.title("Original")
plt.show()

# modifying individual channel 
h_new = h + 30
img_NZ_merged = cv2.merge((h_new, s, v))

img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

# Show the channel
plt.figure(figsize=[15,3])
plt.subplot(141); plt.imshow(h, cmap="gray"); plt.title("H Channel after mod")
plt.subplot(142); plt.imshow(s, cmap="gray"); plt.title("S Channel after mod")
plt.subplot(143); plt.imshow(v, cmap="gray"); plt.title("V Channel after mod")
plt.subplot(144); plt.imshow(img_NZ_rgb); plt.title("Original  after mod")
plt.show()

# open cv store image color as BGR

# save the image
img_NZ_bgr = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2BGR)
cv2.imwrite("New_Zealand_lake_Saved.png", img_NZ_bgr)

Image(filename="New_Zealand_lake_Saved.png")


# Read the image as color
img_NZ_bgr = cv2.imread("New_Zealand_lake_Saved.png", cv2.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is : ", img_NZ_bgr.shape)

# read the image as gray scaled
img_NZ_gry = cv2.imread("New_Zealand_lake_Saved.png", cv2.IMREAD_GRAYSCALE)
print("img_NZ_gry shap (H, W) is : ", img_NZ_gry.shape)