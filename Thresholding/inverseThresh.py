import cv2

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Inverse thresholding

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Inverse Thresholded", thresh_inv)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""
The result is shown below:

The inverse thresholding is the opposite of the simple thresholding. The pixels that are above the threshold are set to 0 and the pixels that are below the threshold are set to 255. This is useful when you want to extract the foreground from the background.
"""