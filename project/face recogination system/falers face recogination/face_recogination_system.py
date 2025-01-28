import cv2
from scipy.datasets import face
import numpy as np
face_cap = cv2.CascadeClassifier("C:/Users/adity/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml") # this file will recognice the face part of human from whole body
video_cam = cv2.VideoCapture(0)# this will enable the camra for face recognation or start the camra
while True :# due to while true the camera will be on for the dueration of time and after preassing the keys it will stop
    ret, video_data = video_cam.read()# reading the images
    if video_data is not None:
        # Convert the frame to grayscale
        col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cap.detectMultiScale(
            col,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(video_data, (x, y), (x + w, y + h), (32,255,255), 2)

    video_data = cv2.flip(video_data, 1)
    cv2.imshow("video live  (prass a for exit() )",video_data) # for showing the image or making a frame of square bracketsli
    if cv2.waitKey(10) == ord("a"): # this comndition is is for wate for off and on press a key it will close the cem
        break 
video_cam.release() # it will release the camera 
cv2.destroyAllWindows()
    