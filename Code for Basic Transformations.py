Code for Basic Transformations

from PIL import Image, ImageOps

# Load the image
image_path = r"C:\Users\Administrator\Downloads\Kareena_Kapoor_at_TOIFA16.jpg"
image = Image.open(image_path)

# 1. **Rotate the image** by a certain angle (e.g., 45 degrees)
def rotate_image(image, angle=45):
    rotated_image = image.rotate(angle)
    rotated_image.show()
    return rotated_image

# 2. **Scale the image** by a certain factor (e.g., 1.5 for scaling up)
def scale_image(image, scale_factor=1.5):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    scaled_image = image.resize((new_width, new_height))
    scaled_image.show()
    return scaled_image

# 3. **Translate (shift)** the image by certain pixels (e.g., 100px right and 50px down)
def translate_image(image, tx=100, ty=50):
    width, height = image.size
    translated_image = Image.new("RGB", (width, height))
    translated_image.paste(image, (tx, ty))
    translated_image.show()
    return translated_image

# Apply transformations
rotated_image = rotate_image(image, 45)   # Rotate by 45 degrees
scaled_image = scale_image(image, 1.5)    # Scale by 1.5x
translated_image = translate_image(image, 100, 50)  # Translate by 100px right, 50px down
