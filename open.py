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
