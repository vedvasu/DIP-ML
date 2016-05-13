import cv2
import numpy as np

img = cv2.imread('sample.png')

# ret,thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#ret,thresh6 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
ret,thresh7 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
# ret,thresh8 = cv2.threshold(gray,150,255,cv2.THRESH_TRUNC)
# ret,thresh9 = cv2.threshold(gray,150,255,cv2.THRESH_TOZERO)
# ret,thresh10 = cv2.threshold(gray,150,255,cv2.THRESH_TOZERO_INV)

blur3 = cv2.medianBlur(thresh7,5)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):

	if cv2.contourArea(contours[i])>2000:
		cv2.drawContours(img,contours,i,(0,255,0),3)

cv2.imshow('blur3',blur3)
#cv2.imshow('gray',gray)
# cv2.imshow('thresh1',thresh1)
# cv2.imwrite('thresh1.jpg',thresh1)
# cv2.imshow('thresh2',thresh2)
# cv2.imshow('thresh3',thresh3)
# cv2.imshow('thresh4',thresh4)
# cv2.imwrite('thresh4.jpg',thresh4)
# cv2.imshow('thresh5',thresh5)
# cv2.imshow('thresh6',thresh6)
cv2.imshow('thresh7',thresh7)
# cv2.imshow('thresh8',thresh8)
# cv2.imshow('thresh9',thresh9)
# cv2.imshow('thresh10',thresh10)

cv2.imshow('img',img)
cv2.imwrite('Image.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()