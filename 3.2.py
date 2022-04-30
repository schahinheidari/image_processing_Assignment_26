import cv2 as cv

img = cv.imread('pic/2.png')
cv.imshow('original', img)
cv.waitKey()
imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)


imgHSV[:,:,2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in imgHSV[:,:,2]]
cv.imwrite('pic/3-2.jpg', imgHSV)
cv.imshow('contrast', cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR))
cv.waitKey()
