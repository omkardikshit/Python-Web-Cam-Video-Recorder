#Use VLC Media Player For Video Watching of Your WebCam
#When You Will Run It It Will Start Capturing You With Your Webcam
#Your Video Will Display Where Your This File Is Located

import cv2
import numpy as np

#if You have 2 webcams then do adjust here 1 or 0 
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video.avi', fourcc,20.0,(640,480))

while True:
   ret, frame = cap.read()
   out.write(frame)
   cv2.imshow ('frame', frame)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
out.release()
cv2.destroyAllWindows()
