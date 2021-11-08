# imports
import albumentations as A
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

def json_annotation_converter(json_path, converted_json_path, image_folder_path, image_save_path,size=(512,512)):
    image_folder_path = image_folder_path
    image_save_path = image_save_path
    images = glob(image_folder_path+"\\*.jpeg")
    H,W = size
    red = [0,255,0]

    json_path = json_path

    with open(json_path) as json_file:
        json_data = json.loads(json_file.read())
        json_file.close()

    list_keys =list(json_data.keys())
    new_json = json_data.copy()
    transform = A.Compose([
        A.Resize(height =H,width=W)
    ], keypoint_params=A.KeypointParams(format='xy'))


    for iidx in range(len(images)):
        list_xy = []
        key_jsondata = list_keys[iidx]
        data = json_data[key_jsondata]
        file_name = data["filename"]
        image = cv2.imread(image_folder_path + file_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        for obj in range(len(data["regions"])):
            print(obj)
            x = data["regions"][obj]["shape_attributes"]["all_points_x"]
            y = data["regions"][obj]["shape_attributes"]["all_points_y"]

            for i in range(len(x)):
                list_xy.append((x[i],y[i]))

        keypoints = list_xy
        transformed = transform(image = image, keypoints=keypoints)
        trans_image = transformed["image"]
        trans_image = cv2.cvtColor(trans_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(image_save_path+file_name,trans_image)
        
        s = 0
        for obj in range(len(new_json[key_jsondata]["regions"])):
            e = len(new_json[key_jsondata]["regions"][obj]["shape_attributes"]["all_points_x"]) + s
            new_xy = transformed["keypoints"][s:e]
            print("kp to json", new_xy)
            x = []
            y = []
            for idx in range(len(new_xy)):
                x.append(int(new_xy[idx][0]))
                y.append(int(new_xy[idx][1]))
        
            new_json[key_jsondata]["regions"][obj]["shape_attributes"]["all_points_x"] = x
            new_json[key_jsondata]["regions"][obj]["shape_attributes"]["all_points_y"] = y
            s = e
            
        with open(converted_json_path, 'w') as fp:
            json.dump(new_json, fp)

#if "__name__" == "__main__":

image_folder_path = "D:\\git_rep\\dataset\\"
json_path = image_folder_path +"annotations.json"
converted_json_path = "D:\\git_rep\\conv\\new_json.json"
image_save_path = "D:\\git_rep\\conv\\"
size = (512,512)
                
json_annotation_converter(json_path,converted_json_path,image_folder_path, image_save_path, size = size)
