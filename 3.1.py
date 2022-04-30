import cv2 as cv

image = cv.imread('pic/2.png')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

contrast = cv.convertScaleAbs(image, alpha=alpha, beta=beta)

#cv.imshow('original', image)
cv.imwrite('pic/3-1.jpg', contrast)
cv.imshow('contrast', contrast)
cv.waitKey()