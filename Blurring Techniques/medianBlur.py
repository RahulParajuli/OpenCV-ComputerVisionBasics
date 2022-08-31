import cv2
img = cv2.imread(
    "/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("original", img)

median = cv2.medianBlur(img, 3)
cv2.imshow("median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
