import cv2

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

# Compare this snippet from GradientsAndEdges/sobel.py:

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)

cv2.waitKey(0)

cv2.destroyAllWindows()
