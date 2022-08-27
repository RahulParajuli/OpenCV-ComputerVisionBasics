import cv2
img = cv2.imread(
    "C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")

cv2.imshow("original", img)

median = cv2.medianBlur(img, 3)
cv2.imshow("median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
