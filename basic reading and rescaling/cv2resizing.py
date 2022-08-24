import cv2 as cv

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimentions = (width, height)
  return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/videos/nature.MOV") # 0 is the id of the camera

while True:
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame)

  cv.imshow("video", frame)
  cv.imshow("resized",frame_resized)
  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()