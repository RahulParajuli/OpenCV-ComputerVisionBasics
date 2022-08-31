import cv2 as cv

capture = cv.VideoCapture("/home/drox/Documents/computervision/ComputerVisionExercise/resources/videos/nature2.MOV") # 0 is the id of the camera
while True:
  isTrue, frame = capture.read()
  cv.imshow("video", frame)
  if cv.waitKey(20) & 0xFF==ord('d'):
    break
capture.release()
cv.destroyAllWindows()
