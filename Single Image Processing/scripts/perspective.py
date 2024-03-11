"""
Operations about perspective transformation
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image, ImageDraw
import cv2
import numpy as np


def perspective_transform_pil(image_path, output_path, points):
    img = Image.open(image_path)

    # Define the four points of perspective transformation
    width, height = img.size
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Transform the perspective
    result = cv2.warpPerspective(np.array(img), matrix, (width, height))

    Image.fromarray(result).save(output_path)


def perspective_transform_cv2(image_path, output_path, points):
    img = cv2.imread(image_path)

    # Define the four points of perspective transformation
    pts1 = np.float32(points)
    pts2 = np.float32(
        [[0, 0], [img.shape[1], 0], [0, img.shape[0]], [img.shape[1], img.shape[0]]]
    )

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Transform the perspective
    result = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))

    cv2.imwrite(output_path, result)


image_path = "Single Image Processing/imgs/Image.jpg"
output_pil_path = "Single Image Processing/outputs/perspective_pil.jpg"
output_cv2_path = "Single Image Processing/outputs/perspective_cv2.jpg"

# Specifies the four points of the perspective transformation
points = [[100, 100], [400, 100], [100, 400], [400, 400]]

perspective_transform_pil(image_path, output_pil_path, points)
perspective_transform_cv2(image_path, output_cv2_path, points)
