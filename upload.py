import pyrebase
import cv2
import os
import sys

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
while True:
    
    ret, frame = cam.read()
    if not ret:
        
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:   
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
               #space 
        img_name = "image.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
cam.release()
cv2.destroyAllWindows()







config={
    "apiKey": "AIzaSyB1-o_JSFTrNaAlwVc5O4u61ykAQY9TGiE",
    "authDomain": "plant-disease-detection-1ce9e.firebaseapp.com",
   "projectId": "plant-disease-detection-1ce9e",
    "databaseURL":"https://plant-disease-detection-1ce9e-default-rtdb.firebaseio.com/",
   "storageBucket": "plant-disease-detection-1ce9e.appspot.com",
    "messagingSenderId": "992347742069",
    "appId": "1:992347742069:web:985b20b5f97000f3643d3c",
    "measurementId": "G-WB81RQV73N"
    }

firebase = pyrebase.initialize_app(config)
storage=firebase.storage()

path_on_cloud="images/test.jpg"
path_local="image.jpg"
storage.child(path_on_cloud).put(path_local)
print("uploaded")
