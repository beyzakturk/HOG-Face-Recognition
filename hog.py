# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:31:11 2022

@author: Beyza
"""

import cv2
from skimage.feature import hog
from skimage import exposure

image = cv2.imread("images/elon_musk.jpeg")
_,hogImage = hog(image, visualize=True)
rescaledImage = exposure.rescale_intensity(image,in_range=(0,10))

cv2.imshow("HOG",hogImage)
cv2.imshow("Rescaled HOG",rescaledImage)