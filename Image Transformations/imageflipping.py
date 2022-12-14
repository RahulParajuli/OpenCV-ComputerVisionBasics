import cv2

img = cv2.imread("/home/drox/Documents/computervision/ComputerVisionExercise/resources/images/shrek.png")

img = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)
cv2.imshow('Original',img)

flip = cv2.flip(img, 1) #it can be 0, 1 or -1 only
cv2.imshow('Flipped1',flip)

flip = cv2.flip(img, 0) #it can be 0, 1 or -1 only
cv2.imshow('Flipped2',flip)

flip = cv2.flip(img, -1) #it can be 0, 1 or -1 only
cv2.imshow('Flipped3',flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
