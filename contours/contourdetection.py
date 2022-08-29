import cv2
import numpy as np

img = cv2.imread(
    "C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/rnr1.jpg")


cv2.imshow("original", img)
cv2.waitKey(0)

blank = np.zeros(img.shape, np.uint8)
cv2.imshow("blank", blank)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)


blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)
cv2.waitKey(0)


# recommended method for edge detection is Canny edge detection
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("Canny Edges", canny)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}, contours(s) found")
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img)
cv2.waitKey(0)


ret, thresh = cv2.threshold(gray, 125, 125, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}, contours(s) found")
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("contours", img)
cv2.waitKey(0)

cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow("blank", blank)
cv2.waitKey(0)

cv2.destroyAllwindows()
