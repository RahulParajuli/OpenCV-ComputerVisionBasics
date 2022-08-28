from inspect import ismemberdescriptor
import cv2
import numpy as np

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/Resources/images/dog3.jpg")
cv2.imshow("original", img)

blank = np.zeros(img.shape[:2], dtype = "uint8")

mask = cv2.rectangle(blank , (img.shape[1]//2-200, img.shape[0]//2), (img.shape[1]//2-400, img.shape[0]//2+200), 255, -1)
cv2.imshow("mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("masked", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
