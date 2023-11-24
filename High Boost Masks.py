import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("C:/Users/Kulasekar/Downloads/tree.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
mask = gray_img - blurred_img
alpha = 2
sharpened_img = gray_img + alpha * mask
sharpened_img = np.clip(sharpened_img, 0, 255).astype(np.uint8)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(sharpened_img, cmap='gray')
plt.title('Sharpened Image')
plt.show()
