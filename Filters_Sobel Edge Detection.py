from PIL import Image, ImageOps, ImageFilter
import numpy as np
import os
from scipy import ndimage

# Load the image
image_path = r"C:\Users\Administrator\Downloads\Kareena_Kapoor_at_TOIFA16.jpg"
image = Image.open(image_path)

# Convert to grayscale for edge detection
gray_image = image.convert('L')

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

# 2. **Edge Detection using Sobel Filter**
def apply_sobel_edge_detection(image):
    # Convert to numpy array
    image_array = np.array(image)

    # Sobel edge detection for both horizontal and vertical gradients
    sobel_x = ndimage.sobel(image_array, axis=0, mode='constant')  # horizontal edges
    sobel_y = ndimage.sobel(image_array, axis=1, mode='constant')  # vertical edges

    # Combine the two gradients
    sobel_edge = np.hypot(sobel_x, sobel_y)  # Compute the magnitude of the gradient
    sobel_edge = np.uint8(sobel_edge / np.max(sobel_edge) * 255)  # Normalize to 0-255 range

    # Convert back to an image
    sobel_image = Image.fromarray(sobel_edge)
    
    # Save and show the sobel edge detection result
    filename = os.path.join(output_dir, "Sobel_Edge_Detection.jpg")
    sobel_image.save(filename)
    sobel_image.show()
    print(f"Image saved as: {filename}")
    return sobel_image

# Apply the filters and save
blurred_image = apply_gaussian_blur(image, 5)   # Apply Gaussian blur with radius of 5
sobel_edges_image = apply_sobel_edge_detection(gray_image)  # Apply Sobel edge detection

