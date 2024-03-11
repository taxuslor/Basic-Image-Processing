"""
Operations about enhancement
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageFilter
import cv2
import numpy as np


def enhance_image_pil(image_path, output_path):
    img = Image.open(image_path)

    # Denoising
    img = img.filter(ImageFilter.MedianFilter(size=3))

    # Detail Enhancement
    img = img.filter(ImageFilter.SHARPEN)
    img.save(output_path)


def enhance_image_cv2(image_path, output_path):
    img = cv2.imread(image_path)

    # Denoising
    img = cv2.medianBlur(img, 3)

    # Detail Enhancement
    img = cv2.detailEnhance(img)

    cv2.imwrite(output_path, img)


enhance_image_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/enhanced_pil.jpg",
)

enhance_image_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/enhanced_cv2.jpg",
)
