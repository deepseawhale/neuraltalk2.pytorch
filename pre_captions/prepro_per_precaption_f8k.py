### Separate dataset images of (default flickr8k) to train/val/test folder(todo: change fixed name train2014/...):
### input args: precaption file, image folder
### default dir of train/val/test will be ../

import json
import logging
import sys
import os
from shutil import copyfile

dir_path = os.path.dirname(os.path.realpath(__file__))
print("curdir: " + dir_path)

# incase for pprint to check structure (for debug)
import pprint
pp = pprint.PrettyPrinter(indent=4)

# check input
if (len(sys.argv) != 3):
    print("error: python thiscript inputjson imgfolder dstfolder, but number of arguments:" + str(len(sys.argv)) + " arguments.")
    exit()

input_json = sys.argv[1]
image_folder = sys.argv[2]

print("imagefolder= " + dir_path  + "/" + image_folder)
imagefolder = dir_path  + "/" + image_folder

trainfolder = dir_path + "/.." + "/train2014"
valfolder   = dir_path + "/.." + "/val2014"
testfolder  = dir_path + "/.." + "/test2014"

# ----------start-----------

# create dst folders and make sure empty
print("-create train2014/val2014/test2014 in ../")
if (not os.path.exists(trainfolder)):
    os.mkdir(trainfolder)
if (not os.path.exists(valfolder)):
    os.mkdir(valfolder)
if (not os.path.exists(testfolder)):
    os.mkdir(testfolder)


# catagorize the images
with open( input_json ) as f:
    data = json.load(f)

filecnt = len(data["images"])
print("-Total number of images in this dataset: " + str(filecnt) + "\n")

for subidx in range(0, filecnt):
    print("copying " + data["images"][subidx]["filename"])
    if data["images"][subidx]["split"] == "train":
        copyfile(imagefolder + "/" + data["images"][subidx]["filename"], trainfolder + "/" + data["images"][subidx]["filename"])
        print("to " + trainfolder)
    elif data["images"][subidx]["split"] == "val":
        copyfile(imagefolder + "/" + data["images"][subidx]["filename"], valfolder + "/" + data["images"][subidx]["filename"])
        print("to " + valfolder)
    else:
        copyfile(imagefolder + "/" + data["images"][subidx]["filename"], testfolder + "/" + data["images"][subidx]["filename"])
        print("to " + testfolder)
print("\nend.")
