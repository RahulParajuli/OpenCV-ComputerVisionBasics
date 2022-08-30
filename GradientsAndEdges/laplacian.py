import cv2
import numpy as np
img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")

cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()