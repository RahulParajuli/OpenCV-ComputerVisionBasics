#Color reading in reality is not the same as color reading in computer vision. The reason is that the human eye is not the same as the computer's. So we get different perspective of the same image plotted using matplotlib and opencv.

import cv2
import matplotlib.pyplot as plt

image = plt.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")
plt.imshow(image)
plt.show()

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()