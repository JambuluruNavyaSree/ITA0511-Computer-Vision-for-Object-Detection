import cv2
import numpy as np
a = cv2.imread("C:/Users/Kulasekar/Downloads/tree.jpg", cv2.IMREAD_GRAYSCALE)
laplacian_kernel = np.array([[0, 1, 0],[1, -4, 1],[0, 1, 0]], dtype=np.float32)
gradient_kernel = np.array([[-1, -1, -1],[-1,  8, -1],[-1, -1, -1]], dtype=np.float32)
a1 = cv2.filter2D(a, -1, laplacian_kernel)
a3 = cv2.filter2D(a, -1, gradient_kernel)
cv2.imshow("Original",a)
cv2.imshow("Laplacian Sharpened Image",a1)
cv2.imshow("Gradient Sharpened Image",a3)
cv2.waitKey(0)
cv2.destroyAllWindows()
