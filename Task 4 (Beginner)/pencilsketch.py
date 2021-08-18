# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 00:15:08 2021

@author: Arkadeep
"""

from IPython.display import display
import matplotlib.pyplot as plt
import cv2
image = cv2.imread(r"D:\Downloads 2\WhatsApp Image 2021-08-18 at 11.56.45.jpeg")
cv2.imshow("Virat Kohli", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Title",gray_image)
inverted_image = 255 - gray_image
cv2.imshow("Atrijor Bara",inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Parijat",pencil_sketch)
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)