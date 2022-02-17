# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:37:17 2022

@author: Beyza
"""

import cv2
import face_recognition

cap = cv2.VideoCapture("video/elon_musk.mp4/")

while True:
    ret,frame =cap.read()
    if ret == False:
        break
    
    faceLocs= face_recognition.face_locations(frame, model="hog")
    color = (0,255,0)
    
    for index,faceLoc in enumerate(faceLocs):
        topLeftY, downRightX, downRightY, topLeftX = faceLoc
        locatedFaces = frame[topLeftY:downRightY, topLeftX:downRightX]
        cv2.imwrite("images/croppedFace.jpg", locatedFaces)
        cv2.rectangle(frame, (topLeftX,topLeftY), (downRightX,downRightY), color,3)
        
        cv2.imshow("Cropped Face",locatedFaces)
        cv2.imshow("Original Image", frame)
        
        if cv2.waitKey(5) & 0xFF == ord("c"):
            break

cap.release()
cv2.destroyAllWindows()        