### Convert flickr8k precaption json (downloaded from:
###          http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip)
### to coco json file as required per https://github.com/nagizeroiw/neuraltalk2.pytorch

import json
import logging
import sys

# incase for pprint to check structure (for debug)
import pprint
pp = pprint.PrettyPrinter(indent=4)

# check input
if (len(sys.argv) != 3):
    print("python thiscript input output, but number of arguments:" + str(len(sys.argv)) + " arguments.")
    print("NOTICE: will use default input dataset_flickr8k_test.json, output dataset_fk8k_cocoformat.json")

#default cfg:
if sys.argv == 3:
    precaption_to_process = sys.argv[1]
    output_file = sys.argv[2]
else:
    precaption_to_process = "dataset_flickr8k_test.json"
    output_file = "output dataset_fk8k_cocoformat.json"

train_folder = 'train2014'
val_folder = 'val2014'
test_folder = 'test2014'


#----------------start----------------
with open( precaption_to_process ) as f:
    data = json.load(f)

filecnt = len(data["images"])
print("Total number of images in this dataset: " + str(filecnt) + "\n")

#for coco dataset: 
#filepath, sentids, filename(COCO_xxx2014_), imgid, split, sentences(tokens, raw, imgid, sentid),cocoid(?)
coco_fields = ["filepath", "sentids", "filename", "imgid", "split", "sentences", "cocoid"]
to_add_fields = []

# predict all dataset's missing field by reading first
cocoid = 0
for keyidx in range(0, len(coco_fields)):
    if (not coco_fields[keyidx] in data["images"][0]):
        print("precaption missing field " + coco_fields[keyidx])
        to_add_fields.append(coco_fields[keyidx])


for subidx in range(0, filecnt):
    #check train or val
    for keyidx in range(0, len(to_add_fields)):
        if to_add_fields[keyidx] == "filepath":
            if data["images"][subidx]["split"] == "train":
                data["images"][subidx][to_add_fields[keyidx]] = train_folder
            elif data["images"][subidx]["split"] == "val":
                data["images"][subidx][to_add_fields[keyidx]] = val_folder
            else:
                data["images"][subidx][to_add_fields[keyidx]] = test_folder
        if to_add_fields[keyidx] == "cocoid":
            data["images"][subidx][to_add_fields[keyidx]] = str(cocoid)
            cocoid = cocoid + 1


# debug just print 2
print("add missing field ---------------")
for subidx in range(0, 1):
    pp.pprint(data["images"][subidx])
print("after reformat: endval ----------")

# write out to one line
print("writing out......")
import json
with open(output_file, 'w') as fot:
    json.dump(data, fot)

print("written to output file: " + output_file + ". END.")