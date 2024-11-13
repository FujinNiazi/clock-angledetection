import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('clock.jpg', cv2.IMREAD_GRAYSCALE)  # Make sure you have a 'clock.jpg' image in the same folder

# Check if image was loaded successfully
if image is None:
    print("Error loading image.")
else:
    print("Image loaded successfully.")

# Use Canny Edge Detection
edges = cv2.Canny(image, 100, 200)

# Plot original and edges images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Edge detected image
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis('off')

# Show the plot
plt.show()
