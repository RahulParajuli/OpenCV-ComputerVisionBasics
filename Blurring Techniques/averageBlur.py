import cv2
img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")
cv2.imshow("original", img)

average = cv2.blur(img, (3,3))
cv2.imshow("average", average)

cv2.waitKey(0)
cv2.destroyAllWindows()
