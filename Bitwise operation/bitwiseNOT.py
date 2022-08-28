import cv2
import numpy as np

blank = np.zeros((400,400), dtype = "uint8")

rectangle = cv2.rectangle(blank.copy(),(30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow("Original rectangle", rectangle)
cv2.imshow("Original circle", circle)

#bitwise NOT operator

bitwiseNOT = cv2.bitwise_not(rectangle)
cv2.imshow("bitwiseNOT", bitwiseNOT)

bitwizeNOTcircle = cv2.bitwise_not(circle)
cv2.imshow("bitwiseNOTcircle", bitwizeNOTcircle)
"""
bitwise NOT operator is used to find the uncommon pixels in image.
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
