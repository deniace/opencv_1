# anotating image
print("Anotating Image")

# import liblary
import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

# %matplotlib inline

# download assets
def download_and_unzip(url, save_path) :
    print(f"Downloading and extracting assets...", end="")

    # Downloading zip file using urllib package
    urlretrieve(url, save_path)

    try :
        # Extracting zip file using the zipfile package
        with ZipFile(save_path) as z :
            # Extract zip  file content in the same directory
            z.extractall(os.path.split(save_path)[0])
        print("Done")
    except:
        print("\nInvalid File.", e)

URL = r"https://www.dropbox.com/s/48hboi1m4crv1tl/opencv_bootcamp_assets_NB3.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"anotating_image/opencv_bootcamp_assets_NB3.zip")

# download if asset zip does not exists
if not os.path.exists(asset_zip_path) :
    download_and_unzip(URL, asset_zip_path)

# Read in an image
image = cv2.imread("anotating_image\Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Display the original image
plt.imshow(image[:, :, ::-1])
plt.title("Apollo Original Image")
plt.show()


# Drawing a line
imageLine = image.copy()

# the line start from (200,100) and end  at (400,100)
# the color of the line is yellow (Recal chat opencv use BGR Format)
# Thickness of line is 5px
# line type is cv2.LINE_AA
# cv2.LINE_8 -> garis biasa, default
# cv2.LINE_4 -> garis 4-connected (Jarang dipakai)
# cv2.LINE_AA -> paling bagus

# cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv2.line(imageLine, (200, 100), (400, 400), (2, 255, 255), thickness=4, lineType = cv2.LINE_AA) 

# display the image
plt.imshow(imageLine[:, :, ::-1])
plt.title("Aolli with line")
plt.show()


# Drawing a circle
imageCircle = image.copy()

# cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
cv2.circle(imageCircle, (900, 600), 100, (0, 0, 255), thickness=5, lineType=cv2.LINE_AA)

# Display the image
plt.imshow(imageCircle[:, :, ::-1])
plt.title("Apolo with circle")
plt.show()

