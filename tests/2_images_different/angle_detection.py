import cv2
import numpy as np

# Function to calculate the angle between two lines
def calculate_angle_between_lines(theta1, theta2):
    angle = abs(np.degrees(theta1 - theta2))  # Convert from radians to degrees
    if angle > 180:
        angle = 360 - angle
    return angle

# Function to filter lines and select the hour hand (closest to vertical)
def select_hour_hand(lines):
    vertical_threshold = np.pi / 12  # Allow more angles for hour hand detection
    hour_hand = None

    for line in lines:
        rho, theta = line[0]

        if np.pi / 2 - vertical_threshold < theta < np.pi / 2 + vertical_threshold:
            hour_hand = (rho, theta)
            break

    if hour_hand is None:
        raise ValueError("Hour hand not detected")

    return hour_hand

# Function to filter lines and select the minute hand (more horizontal)
def select_minute_hand(lines):
    horizontal_threshold = np.pi / 12  # Allow more angles for minute hand detection
    minute_hand = None

    for line in lines:
        rho, theta = line[0]

        if theta < horizontal_threshold or theta > np.pi - horizontal_threshold:
            minute_hand = (rho, theta)
            break

    if minute_hand is None:
        raise ValueError("Minute hand not detected")

    return minute_hand

# Function to filter and group lines
def filter_and_group_lines(lines):
    """
    Filter and group lines detected by Hough transform.
    For simplicity, we can return all lines as they are.
    You can enhance this function to group lines that are close together if necessary.
    """
    return lines  # In this basic version, we just return the lines as they are.

# Function to perform edge detection, line detection, and detect the hour hand
def detect_hour_hand(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error loading image: {image_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Detect lines using Hough Transform
    lines = cv2.HoughLines(edges, 0.1, np.pi / 90, 50)

    if lines is None:
        raise ValueError("No lines detected")

    filtered_lines = filter_and_group_lines(lines)
    hour_hand = select_hour_hand(filtered_lines)

    # Draw the hour hand line on the original image
    rho, theta = hour_hand
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Draw the line in green

    return image, edges, filtered_lines, hour_hand

# Function to perform edge detection, line detection, and detect the minute hand
def detect_minute_hand(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error loading image: {image_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Detect lines using Hough Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)

    if lines is None:
        raise ValueError("No lines detected")

    filtered_lines = filter_and_group_lines(lines)
    minute_hand = select_minute_hand(filtered_lines)

    # Draw the minute hand line on the original image
    rho, theta = minute_hand
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw the line in blue

    return image, edges, filtered_lines, minute_hand
