import cv2 as cv
img = cv.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/rnr1.jpg")
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()