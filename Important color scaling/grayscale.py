import cv2 as cv
img = cv.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/rnr1.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)
cv.destroyAllWindows()
