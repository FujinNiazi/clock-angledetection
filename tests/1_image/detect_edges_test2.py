import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread('clock.jpg', cv2.IMREAD_GRAYSCALE)  # Ensure 'clock.jpg' is in the same folder

# Check if image was loaded successfully
if image is None:
    print("Error loading image.")
else:
    print("Image loaded successfully.")

# Step 1: Edge Detection using Canny
edges = cv2.Canny(image, 100, 200)

# Step 2: Line Detection using Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Create a copy of the original image to draw lines
line_image = np.copy(image)

# Draw the detected lines on the image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        # Draw the line on the image
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue lines

# Step 3: Display the original, edge-detected, and line-detected images
plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Edge Detection
plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis('off')

# Line Detection
plt.subplot(1, 3, 3)
plt.imshow(line_image, cmap='gray')
plt.title("Line Detection")
plt.axis('off')

# Show the plots
plt.show()
