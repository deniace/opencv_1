print("image enhancment")

import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# %matplotlib inline 

# download assets
def download_and_unzip(url, save_path):
    print(f"downloading and extracting assets ", end="")
    
    # Downloading zip file using urllib package
    urlretrieve(url, save_path)
    
    try :
        # Extract zip file using zip file package
        with ZipFile(save_path) as z :
            # Extract zip file in the same directory
            z.extractall(os.path.split(save_path)[0])
            
        print("done")
    except Exception as e :
        print("\nInvalid file.", e)
        
URL = r"https://www.dropbox.com/s/0oe92zziik5mwhf/opencv_bootcamp_assets_NB4.zip?dl=1"

assets_zip_path = os.path.join(os.getcwd(), f"basic_image_enhancment\opencv_bootcamp_assets_NB4.zip")
# assets_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB4.zip")

# download if assets  ZIP does not exists
if not os.path.exists(assets_zip_path):
    download_and_unzip(URL, assets_zip_path)

# Original Image
img_bgr = cv2.imread("basic_image_enhancment/New_Zealand_Coast.jpg.", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2BGR)

# display image pixel
Image(filename="basic_image_enhancment/New_Zealand_Coast.jpg")
plt.imshow(img_rgb)
plt.show()

# addition or Brightness
matrix = np.ones(img_rgb.shape, dtype="uint8") * 50

img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker = cv2.subtract(img_rgb, matrix)

# show the images
plt.figure(figsize=[18, 5])
plt.subplot(131); plt.imshow(img_rgb_darker)    ; plt.title("Darker")
plt.subplot(132); plt.imshow(img_rgb)           ; plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_brighter)  ; plt.title("Brighter")
plt.show()

matrix1 = np.ones(img_rgb.shape) * 0.8
matrix2 = np.ones(img_rgb.shape) * 1.2

img_rgb_darker = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
img_rgb_brighter = np.uint8(cv2.multiply(np.float64(img_rgb), matrix2))

# show the images
plt.figure(figsize=[18,5])
plt.subplot(131); plt.imshow(img_rgb_darker);   plt.title("darker")
plt.subplot(132); plt.imshow(img_rgb)       ;   plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_brighter); plt.title("brighter")
plt.show()


# handling over flow using np.clip
matrix1 = np.ones(img_rgb.shape) * 0.6
matrix2 = np.ones(img_rgb.shape) * 1.5

img_rgb_lower = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
img_rgb_higher = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2), 0, 255))

# show the images
plt.figure(figsize=[18,5])
plt.subplot(131); plt.imshow(img_rgb_lower);    plt.title("lower contrast")
plt.subplot(132); plt.imshow(img_rgb);          plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_higher);   plt.title("higher contrast")
plt.show()


# Image tresholding 
img_read = cv2.imread("basic_image_enhancment/building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_tresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)

# show the image
plt.figure(figsize=[18,5])
plt.subplot(121); plt.imshow(img_read, cmap="gray");    plt.title("original")
plt.subplot(122); plt.imshow(img_tresh, cmap="gray");   plt.title("Thresholded")
plt.show()