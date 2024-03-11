"""
Operations about adjusting color
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageEnhance
import cv2
import numpy as np


def adjust_color_pil(
    image_path, brightness_factor=1.0, contrast_factor=1.0, saturation_factor=1.0
):
    image = Image.open(image_path)

    # brightness
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(brightness_factor)

    # contrast
    enhancer = ImageEnhance.Contrast(brightened_image)
    contrasted_image = enhancer.enhance(contrast_factor)

    # saturation
    enhancer = ImageEnhance.Color(contrasted_image)
    saturated_image = enhancer.enhance(saturation_factor)

    return saturated_image


def adjust_color_cv2(image_path, brightness=0, contrast=1.0, saturation=1.0):
    image = cv2.imread(image_path)

    # brightness
    brightened_image = cv2.convertScaleAbs(image, beta=brightness)

    # contrast
    contrasted_image = cv2.convertScaleAbs(brightened_image, alpha=contrast)

    # saturation
    hsv_image = cv2.cvtColor(contrasted_image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation, 0, 255)
    saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return saturated_image


input_image_path = "Single Image Processing/imgs/Image.jpg"
color_adjusted_image_pil = adjust_color_pil(
    input_image_path,
    brightness_factor=1.5,
    contrast_factor=1.2,
    saturation_factor=1.5,
)
color_adjusted_image_pil.save("Single Image Processing/outputs/color_pil.jpg")

color_adjusted_image_cv2 = adjust_color_cv2(
    input_image_path, brightness=50, contrast=1.5, saturation=1.5
)
cv2.imwrite("Single Image Processing/outputs/color_cv2.jpg", color_adjusted_image_cv2)
