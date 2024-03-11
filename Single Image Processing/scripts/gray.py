"""
Operations about gray scale
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageOps, ImageEnhance
import cv2

origin_image1 = Image.open("Single Image Processing/imgs/Image.jpg")
origin_image2 = cv2.imread("Single Image Processing/imgs/Image.jpg")

# Graying
gray_image1 = origin_image1.convert("L")
gray_image1.save("Single Image Processing/outputs/gray_pil.jpg")

gray_image2 = cv2.cvtColor(origin_image2, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Single Image Processing/outputs/gray_cv2.jpg", gray_image2)

# Binaryzation
threshold1 = 128
binary_image1 = gray_image1.point(lambda x: 0 if x < threshold1 else 255, "1")
binary_image1.save("Single Image Processing/outputs/binary_pil.jpg")

threshold2, binary_image2 = cv2.threshold(gray_image2, 128, 255, cv2.THRESH_BINARY)
cv2.imwrite("Single Image Processing/outputs/binary_cv2.jpg", binary_image2)

# Histogram Equalization
equalized_image1 = ImageOps.equalize(gray_image1)
equalized_image1.save("Single Image Processing/outputs/equalized_pil.jpg")

equalized_image2 = cv2.equalizeHist(gray_image2)
cv2.imwrite("Single Image Processing/outputs/equalized_cv2.jpg", equalized_image2)

# Local Contrast Enhancement
clahe1 = ImageEnhance.Contrast(equalized_image1).enhance(2.0)
clahe1.save("Single Image Processing/outputs/clahe_pil.jpg")

clahe2 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image2 = clahe2.apply(equalized_image2)
cv2.imwrite("Single Image Processing/outputs/clahe_cv2.jpg", clahe_image2)
