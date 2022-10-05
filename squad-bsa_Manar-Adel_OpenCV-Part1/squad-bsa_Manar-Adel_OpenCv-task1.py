
import cv2 as cv
import numpy as np
import random

r  = 0
g  = 0
b= 0

#task 1
x=[(0,50),(50,100),(0,50),(50,100)]
y=[(0,50),(0,50),(50,100),(50,100)]

img=np.zeros((100,100,3),np.uint8) #full frame in black

for i in range (4):
    #choose random color for each square
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    img[x[i][0]:x[i][1], y[i][0]: y[i][1]] = r, g, b



img=cv.resize(img,(200,200))
cv.imshow("resized image",img)
cv.waitKey(0)