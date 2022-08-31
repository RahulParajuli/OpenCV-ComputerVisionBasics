import cv2 as cv
img = cv.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog4.jpg")
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()