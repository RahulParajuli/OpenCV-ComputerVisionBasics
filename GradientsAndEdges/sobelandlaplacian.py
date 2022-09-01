import cv2
import numpy as np

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap", lap)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

combined_sobel = cv2.bitwise_or(sobelx, sobely)

cv2.imshow("sobelx", sobelx)

cv2.imshow("sobely", sobely)

cv2.imshow("combined_sobel", combined_sobel)

canny = cv2.Canny(gray, 100, 200)
cv2.imshow("canny", canny)

cv2.waitKey(0)

cv2.destroyAllWindows()
