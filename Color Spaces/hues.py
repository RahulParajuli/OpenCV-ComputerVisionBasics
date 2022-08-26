import cv2

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog2.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)

hues = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hues", hues)
cv2.waitKey(0)

cv2.destroyAllWindows()