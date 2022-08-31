import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog4.jpg")
cv2.imshow("original Image", img)

plt.figure()
plt.title("color image")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
#color histogram
colors = {"b","g","r"}
for i, col in enumerate(colors):
  hist = cv2.calcHist([img], [i], None, [256], [0,256])
  plt.plot(hist, color = col)
  plt.xlim([0,256])
plt.show()

