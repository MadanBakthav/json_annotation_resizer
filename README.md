# json_annotation_resizer
Had annotated the images? Need to change Image dim again? No need to annotate the images again anymore. This function resizes as well as generates the json annotation needed for the resized images. This program is specifically made to convert VGI annotation format.

This python "file json_annotation_converter.py" consists a function called json_annotation_converter. It takes the following inputs
1. json_path - where your already annotated json exists
2. converted_json_path - Where you would like to save the new annotations
3. image_folder_path - the images should be in same folder as json. The image directory used for convertion depends on this.
4. image_save_path - Where you would like to save the new images
5. size = size which is H and W of new image dim as tuple (H,W)

json_annotation_converter(json_path,converted_json_path,image_folder_path, image_save_path, size = size)


###### Important ########
The old json file and images should exist in same folder.

Folder tree
eg:

Data_folder  -------
             |______images
                      |____ image1.jpeg
                      |_____ image2.jpeg
                      ........
                      |_____ annotation.json
                     
----- Imports ----- 
import albumentations as A
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from glob import glob          
