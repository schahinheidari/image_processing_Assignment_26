import cv2 as cv

image = cv.imread('2.png')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

contrast = cv.convertScaleAbs(image, alpha=alpha, beta=beta)

cv.imshow('original', image)
cv.imshow('contrast', contrast)
cv.waitKey()