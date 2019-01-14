import csv
import cv2
import numpy as np
from scipy import ndimage, misc
import matplotlib.pyplot as plt
data_folder = "../train_data/"
image_folder = data_folder + "IMG/"
print("training folder:", data_folder)
with open(data_folder + "driving_log.csv") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        center_path = line[0]
        image = ndimage.imread(center_path)
        image_flipped = np.fliplr(image)
        misc.imsave('./original.png', image)
        misc.imsave('./flipped.png', image_flipped)
        break