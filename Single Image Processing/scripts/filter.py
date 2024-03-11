"""
Operations about filtering processing
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageFilter
import cv2
import numpy as np


# Smooth
def smooth_image_pil(image_path, output_path):
    image = Image.open(image_path)
    smoothed_image = image.filter(ImageFilter.BLUR)
    smoothed_image.save(output_path)


def smooth_image_cv2(image_path, output_path, kernel_size=(5, 5)):
    image = cv2.imread(image_path)
    smoothed_image = cv2.GaussianBlur(image, kernel_size, 0)
    cv2.imwrite(output_path, smoothed_image)


# Sharpen
def sharpen_image_pil(image_path, output_path):
    image = Image.open(image_path)
    sharpened_image = image.filter(ImageFilter.SHARPEN)
    sharpened_image.save(output_path)


def sharpen_image_cv2(image_path, output_path):
    image = cv2.imread(image_path)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    cv2.imwrite(output_path, sharpened_image)


# Edge Detection
def edge_detection_pil(image_path, output_path):
    image = Image.open(image_path)
    edge_image = image.filter(ImageFilter.FIND_EDGES)
    edge_image.save(output_path)


def edge_detection_cv2(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)
    cv2.imwrite(output_path, edges)


smooth_image_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/smoothed_pil.jpg",
)
smooth_image_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/smoothed_cv2.jpg",
)

sharpen_image_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/sharpened_pil.jpg",
)
sharpen_image_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/sharpened_cv2.jpg",
)

edge_detection_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/edges_pil.jpg",
)
edge_detection_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/edges_cv2.jpg",
)
