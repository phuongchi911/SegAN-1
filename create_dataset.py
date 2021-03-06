import gzip
import shutil
import os
import nibabel as nib
from tifffile import imsave, imread
import numpy as np
import matplotlib.pyplot as plt
import imageio
from array2gif import write_gif
from PIL import Image


def make_dir(path):
    if (not os.path.isdir(path)):
        os.makedirs(path)


image_types = ['flair', 'segmentation', 't1', 't1ce', 't2']
folder_name = 'MICCAI_BraTS2020_TrainingData'
dataset_path = 'dataset'

main_dir = os.listdir(folder_name)
make_dir(dataset_path)
for image_type in image_types:
    make_dir(os.path.join(dataset_path, image_type))

for folder in main_dir:
    cur_dir = os.path.join(folder_name, folder)
    cur_dir_files = os.listdir(cur_dir)
    for i, file in enumerate(cur_dir_files):
        print(file)
        file_path = os.path.join(cur_dir, file)
        save_path = os.path.join(dataset_path, image_types[i], file)
        imgVol = nib.load(file_path)
        npdata = imgVol.get_fdata()
        npdata = npdata.astype(np.uint8)
        for j, image in enumerate(npdata.transpose(2, 0, 1)):
            im = Image.fromarray(image)
            im.save(save_path + str(j) + '.png')
        if 'seg' in file_path:
            break









