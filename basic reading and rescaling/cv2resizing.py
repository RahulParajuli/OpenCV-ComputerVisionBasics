import cv2 as cv
img = cv.imread("resources/images/dog.jpg")
cv.imshow("dog",img)

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimentions = (width, height)
  return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("resources/videos/nature.MOV") # 0 is the id of the camera

# capture = cv.VideoCapture("resources/videos/nature.MOV") # 0 is the id of the camera
while True:
  ret, frame = capture.read()
  frame_resized = rescaleFrame(frame)

  cv.imshow("video", capture)
  cv.imshow("resized",frame_resized)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
