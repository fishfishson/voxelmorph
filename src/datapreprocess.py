import os, glob
import ants
import numpy as np


def get_ACDC_list(root, phase='training'):
    gt_list = glob.glob(os.path.join(root, phase, '*/*gt.nii.gz'))
    gt_list.sort()

    img_list = glob.glob(os.path.join(root, phase, '*/*[0-9].nii.gz'))
    img_list.sort()

    return img_list, gt_list


def iso_resample(img, spacing=None, islabel=False):
    if spacing is None:
        spacing = [1.25, 1.25, 10]
    if islabel:
        img_re = ants.resample_image(img, spacing, False, 1)
    else:
        img_re = ants.resample_image(img, spacing, False, 0)

    return img_re


# def normalize(img):
#
#
#
# def co_reg(img, gt):


def process_pipe(root, phase, ):
    img_list, gt_list = get_ACDC_list(root, phase)

    n = len(img_list)
    for i in range(n):
        img = ants.image_read(img_list[i])
        gt = ants.image_read(gt_list[i])

        #iso-resample
        img_ = iso_resample(img, [2.5, 2.5, 10], islabel=False)
        gt_ = iso_resample(gt, [2.5, 2.5, 10], islabel=True)

        print(img_.shape)

