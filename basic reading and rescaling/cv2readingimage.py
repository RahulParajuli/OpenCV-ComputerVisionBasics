import cv2 as cv
img = cv.imread("resources/images/dog.jpg")
cv.imshow("image", img)
cv.waitKey(0)