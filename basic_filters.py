
import cv2
import os

def main():
    image_path = "D:\Let's learning Coding\Practice of Basic Image processing\Kareena_Kapoor_at_TOIFA16.jpg"
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image at {image_path}")
        return

    os.makedirs("filtered_outputs", exist_ok=True)

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(img, (7, 7), 1.5)
    cv2.imwrite("filtered_outputs/gaussian_blur.jpg", gaussian)

    # Sobel Edge Detection (X direction)
    sobelx = cv2.Sobel(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 1, 0, ksize=5)
    cv2.imwrite("filtered_outputs/sobel_x.jpg", cv2.convertScaleAbs(sobelx))

    # Laplacian Filter
    laplacian = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F)
    cv2.imwrite("filtered_outputs/laplacian.jpg", cv2.convertScaleAbs(laplacian))

    print("Filtered images saved in filtered_outputs/")

if __name__ == "__main__":
    main()
    
