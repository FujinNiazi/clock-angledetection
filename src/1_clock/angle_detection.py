# angle_detection.py
import cv2
import numpy as np

# Function to calculate the angle between two lines
def calculate_angle_between_lines(theta1, theta2):
    angle = abs(np.degrees(theta1 - theta2))  # Convert from radians to degrees
    if angle > 180:
        angle = 360 - angle
    return angle

# Function to filter lines that are too close together
def filter_and_group_lines(lines, distance_threshold=50, angle_threshold=np.pi / 90):
    filtered_lines = []
    for line in lines:
        rho, theta = line[0]
        add_line = True

        # Compare the current line with the lines in filtered_lines
        for filtered_rho, filtered_theta in filtered_lines:
            # If the lines are close in distance (rho) and angle (theta), group them
            if abs(rho - filtered_rho) < distance_threshold and abs(theta - filtered_theta) < angle_threshold:
                add_line = False
                break

        if add_line:
            filtered_lines.append((rho, theta))

    return filtered_lines

# Function to perform edge detection, line detection, and calculate the angle
def detect_angle(image_path):
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if image was loaded successfully
    if image is None:
        raise ValueError(f"Error loading image: {image_path}")

    # Step 1: Edge Detection using Canny
    edges = cv2.Canny(image, 100, 200)

    # Step 2: Line Detection using Hough Line Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

    # Check if any lines were detected
    if lines is None or len(lines) < 2:
        raise ValueError("Not enough lines detected to calculate the angle")

    # Step 3: Filter and group the lines to avoid detecting both edges of thick hands
    filtered_lines = filter_and_group_lines(lines)

    # Check if there are at least two distinct lines after filtering
    if len(filtered_lines) < 2:
        raise ValueError("Not enough distinct lines detected after filtering")

    # Extract theta values of the first two filtered lines
    theta1, theta2 = filtered_lines[0][1], filtered_lines[1][1]

    # Calculate the angle between the two lines
    angle = calculate_angle_between_lines(theta1, theta2)

    return image, edges, filtered_lines, angle
