# detect_edges.py
import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from angle_detection import detect_angle

# Define the path to your image
image_path = Path('data/images/clock1.jpg')

# Step 1: Detect angle between clock hands
try:
    image, edges, filtered_lines, angle = detect_angle(image_path)

    # Create a copy of the original image to draw lines
    line_image = np.copy(image)

    # Draw the detected filtered lines on the image
    if filtered_lines is not None:
        for rho, theta in filtered_lines[:2]:  # Assuming we only need the first two lines
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

    # Step 2: Display the original, edge-detected, and line-detected images
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

    # Line Detection with Angle
    plt.subplot(1, 3, 3)
    plt.imshow(line_image, cmap='gray')
    plt.title(f"Line Detection (Angle: {angle:.2f}°)")
    plt.axis('off')

    # Show the plots
    plt.show()

    # Print the calculated angle
    print(f"Angle between the clock hands: {angle:.2f} degrees")

except ValueError as e:
    print(e)
