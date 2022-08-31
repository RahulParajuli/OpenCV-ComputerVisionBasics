import cv2 as cv
img = cv.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")
cv.imshow("image", img)
cv.waitKey(0)