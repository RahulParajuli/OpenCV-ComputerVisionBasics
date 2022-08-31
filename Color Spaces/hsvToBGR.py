import cv2

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

cv2.imshow("original image", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

#conversion of HSV to BGR color format
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV to BGR", bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()