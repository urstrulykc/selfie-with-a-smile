import requests
import cv2
import numpy as np
import imutils

#replace the below url with your own. Makesure that you add "/shot.jpg" at last.
url="https://ibb.co/KDry842/shot.jpg"

#while loop for continuous fetching of data
while true:
   img_res=requests.get(url)
   img_arr=np.array(bytearray(img_res.content),dtype=np.uint8)
   img= cv2.imdecode(img_arr,-1)
   cv2.imshow("Android_cam",img)
   #press esc key to exit
   if cv2.waitkey(1)==27:
       break
cv2.destroyAllWindows()
video_capture=cv2.VideoCapture(0)
While video_capture.isOpened():
  #captures videocapture frame by frame
    _, frame=video_capture.read()
  #to capture image in monochrome
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #calls the detect() function
    canvas=detect(gray,frame)
  #displays the result on camera feed
    cv.imshow('Video',canvas)
  #the control breaks once q key is pressed
    if cv2.waitkey(1)& 0xff ==ord('q'):
       break
  #release the capture once all the processing is done
  video_capture.release()
  cv2.destroyAllWindows()
