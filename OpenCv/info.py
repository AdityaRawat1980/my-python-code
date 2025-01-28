import cv2
import numpy as np
img = cv2.imread("ar.jpeg")
# print(img) it shows the colour combination of pixl in the given image 
reimg = cv2.resize(img,(400,400))
cv2.imshow("Image", reimg)
cv2.waitKey(0)
cv2.destroyWindow
v = np.array([[1,2,1,2],[1,2,1,2]])