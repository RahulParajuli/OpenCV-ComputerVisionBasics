#accessing the web camera

import cv2 as cv
capture = cv.VideoCapture(0) # 0 is the id of the camera
while True:
  isTrue, frame = capture.read() # isTrue is a boolean, frame is the image
  cv.imshow("video", frame) # show the image
  if cv.waitKey(20) & 0xFF==ord('d'):
    break # exit the loop
capture.release() # release the camera
cv.destroyAllWindows() # close all the windows