import cv2 as cv

def rescaleFrame(frame, scale=0.75):
  #works with images, videos, live videos
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimentions = (width, height)
  return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("/home/drox/Documents/computervision/ComputerVisionExercise/resources/videos/nature.MOV") # 0 is the id of the camera

def changeResolution(frame, width, height):
  #works only with live videos
  capture.set(3,width)
  capture.set(4,height)

  return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

while True:
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame)

  cv.imshow("video", frame)
  cv.imshow("resized",frame_resized)
  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()