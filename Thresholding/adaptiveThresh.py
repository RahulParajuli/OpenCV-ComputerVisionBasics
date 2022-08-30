import cv2
img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Adaptive thresholding

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)

cv2.imshow("Adaptive Mean Thresholded", thresh)

gaussianthresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)

cv2.imshow("Adaptive Gaussian Thresholded", gaussianthresh)

cv2.waitKey(0)

cv2.destroyAllWindows()
