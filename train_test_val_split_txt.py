"""
Use case:
After using train_test_val_split, image files get split into three folders
txt labels can be moved accordingly using this script
"""

import sys
import os
import shutil

def return_file_names(images_folder):
        file_names = []
        for file in os.listdir(images_folder):
            file_names.append(file.split('.')[0])
        return file_names

if len(sys.argv)!=4:
    print("Some of the Command line args missing")
else:
    images_folder = sys.argv[1]
    img_file_names = return_file_names(images_folder)

    txt_folder = sys.argv[2]
    txt_file_names = return_file_names(txt_folder)

    output_folder = sys.argv[3]
    for file in img_file_names:
        file_to_move = r"{}.txt".format(file)
        if file_to_move in os.listdir(txt_folder):
             shutil.move(os.path.join(txt_folder,file_to_move),r"{}".format(output_folder))