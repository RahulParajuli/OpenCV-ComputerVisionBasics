
"""
Histograms for the images file is nothing but the frequency of pixels present in the image.
BGR is the content of color present to form the image.
so we can plot such a graph for each color channel with a histogram.
Checks distribution of colors in the image.
"""

import matplotlib.pyplot as plt
import cv2

img = cv2.imread("c:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog.jpg")
cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()