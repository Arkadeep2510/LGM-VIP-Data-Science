# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 00:15:08 2021

@author: Arkadeep
"""
# Importing The Libraries
import cv2

# Sample Image
image = cv2.imread(r"D:\Downloads 2\viratkohli.jpg")
# cv2.imshow("Virat Kohli", image)
cv2.waitKey(0)

# Converting to Grey Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image",gray_image)
cv2.waitKey(0)

# Inverting the image
inverted_image = 255 - gray_image
# cv2.imshow("Inverted Image",inverted_image)
cv2.waitKey(0)

# Converting the image to blur image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
# cv2.imshow("Blurred Image",inverted_blurred)
cv2.waitKey(0)

# Showing The Two Images Together
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
# cv2.imshow("pencil sketch",pencil_sketch)
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)