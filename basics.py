import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat' , img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#blur
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)



#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#resize

resized = cv.resize(img,(500,500))
cv.imshow('Resized', resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)