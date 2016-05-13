import cv2
import numpy as np

img = cv2.resize(cv2.imread('sample2.png'),(800,600))
# h,w,t = img.shape
# img = img[h/2:h,:,:]
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret,thresh6 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
ret,thresh7 = cv2.threshold(gray,80,255,cv2.THRESH_BINARY_INV)
# ret,thresh8 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
# ret,thresh9 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
# ret,thresh10 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)

contours, hierarchy = cv2.findContours(thresh7,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,contours,-1,(0,255,0),1)

contour_rect=[]
i=0
# print len(contours)
for i in xrange(len(contours)):
	area = cv2.contourArea(contours[i])
	[intX, intY, intWidth, intHeight]=cv2.boundingRect(contours[i])
	if (area > 400 and area < 800) or ( float(intWidth)/intHeight > 3.0 and float(intWidth)/intHeight < 5.0 ):
		#cv2.drawContours(img,contours,i,(0,255,0),2)
		print area
		contour_rect.append(cv2.boundingRect(contours[i]))
		i+=1

for i in range(len(contour_rect)):
	
	print intX,intY,intHeight,intWidth,float(intWidth)/intHeight	
	cv2.rectangle(img,(intX, intY),(intX + intWidth, intY + intHeight),(0, 0, 255),2)
	imgRoi = img[intY:intY+intHeight,intX:intX+intWidth,:]
	cv2.imshow('imgRoi'+str(i),imgRoi)
	cv2.imwrite('imgRoi'+str(i)+'.jpg',imgRoi)

#cv2.imshow('thresh1',thresh1)
# cv2.imshow('thresh2',thresh2)
# cv2.imshow('thresh3',thresh3)
# cv2.imshow('thresh4',thresh4)
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