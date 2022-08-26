import cv2

img = cv2.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/dog3.jpg")
cv2.imshow("original", img)

labs = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("labs", labs)

hues = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)
cv2.imshow("hues", hues)

#conversion of labs format to BGR color format
labs_bgr = cv2.cvtColor(labs, cv2.COLOR_LAB2BGR)
cv2.imshow("labs to BGR", labs_bgr)

#conversion of hues format to BGR color format
hues_bgr = cv2.cvtColor(hues, cv2.COLOR_HSV2BGR)
cv2.imshow("hues to BGR", hues_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()