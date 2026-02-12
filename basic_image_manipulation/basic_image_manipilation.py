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

# plt.figure(figsize=[15,4])

# plt.imshow(img_NZ_rgb)
# plt.show()
# plt.subplot(141); plt.imshow(img_NZ_rgb); plt.title("originale")

# crop out the middle region of the image
cropped_region = img_NZ_rgb[200:400, 300:600]

# plt.imshow(cropped_region)
# plt.show()

# plt.subplot(142); plt.imshow(cropped_region); plt.title("cropped")
plt.imshow(cropped_region)
plt.title("Cropped Region")
plt.show()

# Resizing Images
resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)
plt.imshow(resized_cropped_region_2x)
plt.title("Resized Cropped region 2x")
plt.show()

# Specifying exact size of the output image
desired_width = 110
desired_height = 200

dim = (desired_width, desired_height)

# resize background image to sae size as logo image
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.title("resized Cropped Region")
plt.show()

# Resize while maintaining aspect ratio
# Method 2 : using dsize
desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)
print(dim)

# Resized image
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.title("resized maintain aspect ratio")
plt.show()


# Let's actually show the (cropped) resized image.
# swap channel order
# cv2.imwrite("basic_image_manipulation/resized_cropped_region_2x_no_swap.png", resized_cropped_region_2x) # kalo ga di swap warnanya jadi BGR
resized_cropped_region_2x = resized_cropped_region_2x[:, :, ::-1]

# save resized image to disk 
cv2.imwrite("basic_image_manipulation/resized_cropped_region_2x.png", resized_cropped_region_2x)

# Displaay the cropped and resized image
Image(filename="basic_image_manipulation/resized_cropped_region_2x.png")
# plt.imshow

# swap the channel ro RGB
cropped_region = cropped_region[:, :, ::-1]

# save the cropped region
cv2.imwrite("basic_image_manipulation/cropped_region.png", cropped_region)

# display the cropped and resized image
Image(filename="basic_image_manipulation/cropped_region.png")


# Flipping images

img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1) # Horizontal flip
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0) # vertical flip
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1) # both flip

plt.figure(figsize=(15,5))
plt.subplot(141); plt.imshow(img_NZ_rgb_flipped_horz); plt.title("Horizontal flip")
plt.subplot(142); plt.imshow(img_NZ_rgb_flipped_vert); plt.title("Vertical flip")
plt.subplot(143); plt.imshow(img_NZ_rgb_flipped_both); plt.title("both flip")
plt.subplot(144); plt.imshow(img_NZ_rgb); plt.title("Original")

plt.show()