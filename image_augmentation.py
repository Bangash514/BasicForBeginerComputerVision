
from PIL import Image
from torchvision import transforms

# Your image path
#image_path = r"C:\Users\Administrator\Downloads\Kareena_Kapoor_at_TOIFA16.jpg"
image_path = "D:\Let's learning Coding\Practice of Basic Image processing\Kareena_Kapoor_at_TOIFA16.jpg"

# Load image
img = Image.open(image_path)

# Define some augmentations
augmentations = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(30),
    transforms.ColorJitter(brightness=0.5, contrast=0.5),
    transforms.RandomResizedCrop(224)
])

# Apply augmentations
augmented_img = augmentations(img)

# Show the original and augmented images
img.show(title="Original Image")
augmented_img.show(title="Augmented Image")
