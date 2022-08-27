# most used bluring technique
# bilateral bluring is used to reduce noise while keeping edges sharp

import cv2

img = cv2.imread("c:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")

cv2.imshow("original", img)

bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow("bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
