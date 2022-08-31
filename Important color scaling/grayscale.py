import cv2 as cv
img = cv.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/rnr1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)
cv.destroyAllWindows()
