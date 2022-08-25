import cv2 as cv

img = cv.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/rnr1.jpg")
canny = cv.Canny(img, 100, 200)
cv.imshow("canny", canny)
cv.waitKey(0)
cv.destroyAllWindows()

#with blur and canny tor reduce some of the edges
img = cv.imread("C:/Users/batman/Desktop/mypractices/computer vision/ComputerVisionExercise/resources/images/rnr1.jpg")
blur= cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 100,200)
cv.imshow("Canny Edges", canny)
cv.waitKey(0)
cv.destroyAllWindows()

#dialating the images
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dilated", dilated)
cv.waitKey(0)

#eroding the images
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow("eroded", eroded)
cv.waitKey(0)
cv.destroyAllWindows()

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)
cv.waitKey(0)
cv.destroyAllWindows()

#cropping
cropped = resized[0:200, 0:200]
cv.imshow("cropped", cropped)
cv.waitKey(0)
cv.destroyAllWindows()