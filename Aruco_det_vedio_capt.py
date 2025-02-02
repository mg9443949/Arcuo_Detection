#accesing the camera for taking picture
import numpy as np
import matplotlib as plt
import cv2 as cv
#one can change the index values accroding to the device for access 
cap = cv.VideoCapture(0)   #index 0 means the inbuilt camera 
if not cap.isOpened():
    print("cannot access the camera")
while True:
    
    ret,frame = cap.read()
    if not ret:
        print("cannot access the camera")
    cv.imshow("frame",frame)
    aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_1000)
    parameters = cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(aruco_dict,parameters)
    corners,ids,rejected = detector.detectMarkers(frame)
    print("the detctors are : ",ids)
    if ids is not None:
        cv.aruco.drawDetectedMarkers(frame,corners,ids)
        cv.imshow("detect@aruco",frame)
        if cv.waitKey(25) == ord('q'):
            break

