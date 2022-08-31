
import cv2 as cv
import numpy as np

img = cv.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/dog3.jpg")
cv.imshow("original", img)

#translation
def translate(img, x, y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimentions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimentions)

# -x --> Left
# +x --> Right
# -y --> Up
# +y --> Down

translated = translate(img,100,100)
cv.imshow("translated1",translated)

translated = translate(img,-100,-100)
cv.imshow("translated2",translated)

translated = translate(img,-100,100)
cv.imshow("translated3",translated)

translated = translate(img,100,-100)
cv.imshow("translated4",translated)

cv.waitKey(0)
cv.destroyAllWindows()

#image will shift by x and y pixels