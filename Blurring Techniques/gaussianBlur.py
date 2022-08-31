import cv2
img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("original", img)

gaussian = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow("gaussian", gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
