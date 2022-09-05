import cv2
import numpy as np

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# absolute laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

#displaying laplacian image
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()