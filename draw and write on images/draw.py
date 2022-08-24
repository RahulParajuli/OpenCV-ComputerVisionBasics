import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8') # create a blank image
cv.imshow("blank", blank) # show the blank image

#paint the images with certain color
blank[200:300, 300:400] = 0,0,255 # paint the blank image with green
cv.imshow("Green Line", blank) # show the blank image


#draw a rectangle
cv.rectangle(blank, (0,0), (150,150), (0,255,0), thickness=-1) # draw a rectangle with green color and thickness 3
#thickness can be positive for bounding boxes and negative for filled rectangles


# alternatively,
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2) # draw a rectangle with green color and thickness -1
cv.imshow("Rectangle", blank) # show the blank image
cv.waitKey(0)