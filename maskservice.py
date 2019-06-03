# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:38:01 2019

@author: Abhishek Tripathi
"""

import tensorflow as tf;
import keras
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt
import os 
#os.chdir('./Mask_RCNN/samples')
ROOT_DIR = os.path.abspath("")
# Import Mask RCNN
sys.path.append(ROOT_DIR)

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
from mrcnn import visualize
from mrcnn import serveVisual
sys.path.append(os.path.join(ROOT_DIR, "samples/balloon"))  # To find local version
import balloon

COCO_MODEL_PATH = os.path.join(ROOT_DIR, "var1\\mask_rcnn_forest_0006.h5")

config = balloon.BalloonConfig()
class InferenceConfig(config.__class__):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
class MaskService():
    class_names = ['BG','forest']
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")
    config = InferenceConfig()
    model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
    model.load_weights(COCO_MODEL_PATH, by_name=True)


def serviceImage1():
    mask1 = MaskService()
    path = 'var1/1.jpg'
    image = skimage.io.imread(path)
    results = mask1.model.detect([image], verbose=0)
    r = results[0]
    return serveVisual.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                            mask1.class_names, r['scores'])
