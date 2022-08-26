import cv2
import matplotlib.pyplot as plt

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")

cv2.imshow("original", img)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()