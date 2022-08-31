import cv2
import numpy as np

img = cv2.imread(
    "/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")

blank = np.zeros(img.shape, np.uint8)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)


# recommended method for edge detection is Canny edge detection
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("Canny Edges", canny)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}, contours(s) found")
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img)


ret, thresh = cv2.threshold(gray, 125, 125, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}, contours(s) found")
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img)

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow("blank", blank)
cv2.waitKey(0)

cv2.destroyAllwindows()
