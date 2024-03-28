"""
Operations about histogram
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageDraw
import cv2
import matplotlib.pyplot as plt

img_pil = Image.open("../imgs/Image.jpg")
img_cv2 = cv2.imread("../imgs/Image.jpg")

# PIL
hist_pil = img_pil.histogram()
plt.plot(hist_pil)
plt.title("Histogram")
plt.show()
plt.clf()

# CV2
plt.hist(img_cv2.ravel(), 256, [0, 256])
plt.title("Histogram")
plt.show()
plt.clf()

hist_cv2 = cv2.calcHist([img_cv2], [0], None, [256], [0, 256])
plt.plot(hist_cv2)
plt.title("Histogram")
plt.show()
plt.clf()
