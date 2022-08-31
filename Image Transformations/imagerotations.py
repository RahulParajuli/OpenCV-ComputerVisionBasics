# rotation
import cv2

img = cv2.imread(
    "/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog2.jpg")
img = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Original', img)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)
    return cv2.warpAffine(img, rotMat, dimentions)


rotated = rotate(img, 90)
cv2.imshow("rotated1", rotated)

rotated = rotate(img, -90)
cv2.imshow("rotated2", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
