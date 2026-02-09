import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# matplotlib inline #  is a "magic function" used in Jupyter notebooks and IPython shells to display Matplotlib plots and visualizations directly within the output cell, rather than in a separate window
def download_and_unzip(url, save_path):
    print(f"Downloading and extract assets....", end="")

    # Downloading zip file using urllib package
    urlretrieve(url, save_path)

    try :
        # extracting  zip file using the zipfile package
        with ZipFile(save_path) as z:
            # Extrac zip file contents in the same directory
            z.extractall(os.path.split(save_path)[0])
        
        print("done")

    except : 
        print("\nInvalid File ...", e)

URL = r"https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1"
asset_zip_path = os.path.join(os.getcwd(), f"basic_image_manipulation\opencv_bootcamp_assets_NB2.zip")

# download if asset zip does not exixts
if not os.path.exists(asset_zip_path) :
    download_and_unzip(URL, asset_zip_path)

# original checker board image
# read image as gray scale
cb_img = cv2.imread("checkerboard_18x18.png", 0)

# set color map to gray scale for proper rendering
plt.imshow(cb_img, cmap="gray")
print(cb_img)
# plt.show()

# Access individual pixels
# print the first pixel of the first black box
print(cb_img[0,0])

# print the first white pixel to the right of the first black box
print(cb_img[0,6])

# modifying Image pixel
cb_img_copy = cb_img.copy()
cb_img_copy[2,2] = 200
cb_img_copy[2,3] = 200
cb_img_copy[3,2] = 200
cb_img_copy[3,3] = 200

# same as above
# cb_img_copy[2:3, 2:3] = 200

plt.imshow(cb_img_copy, cmap="gray")
print(cb_img_copy)
# plt.show()

# cropping image
img_NZ_bgr = cv2.imread("basic_image_manipulation/New_Zealand_Boat.jpg", cv2.IMREAD_COLOR)
img_NZ_rgb = img_NZ_bgr[:, :, ::-1]

plt.figure(figsize=[15,4])

# plt.imshow(img_NZ_rgb)
# plt.show()
plt.subplot(141); plt.imshow(img_NZ_rgb); plt.title("originale")

# crop out the middle region of the image
cropped_region = img_NZ_rgb[200:400, 300:600]

# plt.imshow(cropped_region)
# plt.show()

plt.subplot(142); plt.imshow(cropped_region); plt.title("cropped")
plt.show()