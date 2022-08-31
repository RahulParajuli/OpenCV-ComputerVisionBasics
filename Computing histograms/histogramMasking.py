import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")

cv2.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2 + 45),100, 255, -1)
cv2.imshow("mask", mask)

maskedImg = cv2.bitwise_and(gray, gray, mask=mask)
cv2.imshow("maskedImg", maskedImg)

gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
