"""
Operations about size
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image
import cv2


# Resize
def resize_image_pil(image_path, output_path, new_size):
    image = Image.open(image_path)
    resized_image = image.resize(new_size)
    resized_image.save(output_path)


def resize_image_cv2(image_path, output_path, new_size):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, new_size)
    cv2.imwrite(output_path, resized_image)


# Crop
def crop_image_pil(image_path, output_path, left, top, right, bottom):
    image = Image.open(image_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)


def crop_image_cv2(image_path, output_path, left, top, right, bottom):
    image = cv2.imread(image_path)
    cropped_image = image[top:bottom, left:right]
    cv2.imwrite(output_path, cropped_image)


resize_image_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/resized_pil.jpg",
    (300, 200),
)
resize_image_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/resized_cv2.jpg",
    (300, 200),
)

crop_image_pil(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/cropped_pil.jpg",
    100,
    100,
    400,
    300,
)
crop_image_cv2(
    "Single Image Processing/imgs/Image.jpg",
    "Single Image Processing/outputs/cropped_cv2.jpg",
    100,
    100,
    400,
    300,
)
