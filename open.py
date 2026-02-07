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
