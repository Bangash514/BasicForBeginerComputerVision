import pydicom
import matplotlib.pyplot as plt

# Path to your DICOM image file
dicom_path = r"path"

# Read the DICOM file
ds = pydicom.dcmread(dicom_path)

# Extract image pixel array
img = ds.pixel_array

# Show image
plt.imshow(img, cmap='gray')
plt.title("DICOM Image")
plt.axis('off')
plt.show()

 
