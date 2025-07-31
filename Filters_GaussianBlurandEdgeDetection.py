
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 14:58:14 2025

@author: Administrator
"""

#Code for Filters (Gaussian Blur and Edge Detection)
from PIL import Image, ImageFilter
import os

# Load the image
image_path = r"C:\Users\Administrator\Downloads\Kareena_Kapoor_at_TOIFA16.jpg"
image = Image.open(image_path)

# Directory to save filtered images
output_dir = r"C:\Users\Administrator\Downloads\Filtered_Images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 1. **Gaussian Blur**
def apply_gaussian_blur(image, radius=5):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    filename = os.path.join(output_dir, f"Gaussian_Blur_{radius}.jpg")
    blurred_image.save(filename)
    blurred_image.show()
    print(f"Image saved as: {filename}")
    return blurred_image

# 2. **Edge Detection (using Sobel Filter)**
def apply_edge_detection(image):
    edges_image = image.filter(ImageFilter.FIND_EDGES)
    filename = os.path.join(output_dir, "Edge_Detection.jpg")
    edges_image.save(filename)
    edges_image.show()
    print(f"Image saved as: {filename}")
    return edges_image

# Apply the filters and save
blurred_image = apply_gaussian_blur(image, 5)   # Apply Gaussian blur with radius of 5
edges_image = apply_edge_detection(image)       # Apply edge detection (Sobel)
