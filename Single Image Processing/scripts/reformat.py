"""
Operations about converting the format of an image
Using the Pillow Library or OpenCV Library.
"""

from PIL import Image
import cv2

# Convert a jpg to png
# Pillow
origin_image1 = Image.open("Single Image Processing/imgs/Image.jpg")
# Save the original image as a PNG format
# (Note: This operation doesn't actually change the format, it just saves a copy of the image in PNG format)
png_image1 = origin_image1.save("Single Image Processing/outputs/jpg2png1.png")

# OpenCV
origin_image2 = cv2.imread("Single Image Processing/imgs/Image.jpg")
# Save the original image as a PNG format using OpenCV
# (Note: Similar to PIL, this operation saves a copy of the image in PNG format)
cv2.imwrite("Single Image Processing/outputs/jpg2png2.png", origin_image2)

# Convert a gif to png
# Pillow
gif_image1 = Image.open("Single Image Processing/imgs/GIF.gif")
# Save the first frame
gif2jpg1 = gif_image1.save("Single Image Processing/outputs/gif2jpg1.png")
# Save all the frames
total_frames = gif_image1.n_frames
output_path_prefix = "Single Image Processing/outputs/AllFrames/frame"
for frame_number in range(total_frames):
    gif_image1.seek(frame_number)
    output_filename = f"{output_path_prefix}_{frame_number}.png"
    gif_image1.save(output_filename)

# OpenCV
# ...
