#Color reading in reality is not the same as color reading in computer vision. The reason is that the human eye is not the same as the computer's. So we get different perspective of the same image plotted using matplotlib and opencv.

#matplotlib takes the image as a numpy array and plots it. Opencv takes the image as a numpy array and plots it with BGR features.

import cv2
import matplotlib.pyplot as plt

image = plt.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")
plt.imshow(image)
plt.show()

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()