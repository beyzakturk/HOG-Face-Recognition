# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:16:03 2022

@author: Beyza
"""

import cv2
import face_recognition

image = cv2.imread("images/elon_musk.jpeg/")
faceLocs= face_recognition.face_locations(image)
color = (0,255,0)

for index,faceLoc in enumerate(faceLocs):
    topLeftY, downRightX, downRightY, topLeftX = faceLoc
    locatedFaces = image[topLeftY:downRightY, topLeftX:downRightX]
    cv2.imwrite("images/croppedFace.jpg", locatedFaces)
    cv2.rectangle(image, (topLeftX,topLeftY), (downRightX,downRightY), color,3)
    
    cv2.imshow("Cropped Face",locatedFaces)
    cv2.imshow("Original Image", image)
    
    