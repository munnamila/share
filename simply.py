# simplify the result of the object_recognition
import numpy as np
import glob
from tqdm import tqdm
import time
import os

def select_teacher_field(object_recognition):
    # 一つのファイルのデモを簡潔にする

    object_recognition = object_recognition['instances']
    pred_masks = object_recognition.pred_masks

    pred_classes = list(object_recognition.pred_classes)

    try:
        h, w = object_recognition[0].image_size
    except:
        h, w = object_recognition.image_size

    # 教宫領域の適定
    try:
        max_index = pred_classes.index(0)
        teacher_field = pred_masks[max_index].numpy()
    except:
        teacher_field = np.zeros((h,w), dtype=bool)

    # エンコーディング
    compressed_data = np.packbits(teacher_field)# encoding
    size = np.array([h, w])

    return compressed_data, size

