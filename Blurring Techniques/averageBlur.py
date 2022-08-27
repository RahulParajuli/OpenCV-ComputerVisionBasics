import cv2
img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")
cv2.imshow("original", img)

average = cv2.blur(img, (3,3))
cv2.imshow("average", average)

cv2.waitKey(0)
cv2.destroyAllWindows()
