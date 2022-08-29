import cv2
import numpy as np

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/Resources/images/dog3.jpg")
cv2.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

rectangle =  cv2.rectangle(blank.copy(), (80,80), (500,400), 255, -1)

circle = cv2.circle(blank.copy(), (img.shape[1]//2-200, img.shape[0]//2),100, 255, -1)

mask = cv2.bitwise_or(rectangle, circle)

cv2.imshow("mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("masked", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
