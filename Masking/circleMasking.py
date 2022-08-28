import cv2
import numpy as np

img = cv2.imread("c:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")
cv2.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45),100, 255, -1)
cv2.imshow("mask", mask)

maskedImg = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("maskedImg", maskedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
