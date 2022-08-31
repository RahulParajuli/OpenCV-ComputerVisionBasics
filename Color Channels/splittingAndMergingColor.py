import cv2
import numpy as np

#reading image and splitting it into channels
img = cv2.imread(
    "/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")

blank = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("original", img)
b, g, r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)

# it is shown as grayscale because grayscale has the single channel operaiton
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# merging the channels
merged = cv2.merge([b, g, r])
cv2.imshow("Merged image", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
