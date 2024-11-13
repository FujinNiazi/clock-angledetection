import cv2
import numpy as np

# Function to calculate the angle between two lines (in radians)
def calculate_angle_between_lines(theta1, theta2):
    angle = abs(np.degrees(theta1 - theta2))  # Convert from radians to degrees
    if angle > 180:
        angle = 360 - angle
    return angle


def detect_longest_line(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error loading image: {image_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)  # Adjusted Canny thresholds

    # Use Probabilistic Hough Transform for better control
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)

    if lines is None:
        raise ValueError("No lines detected")

    # Find the longest line
    longest_line = None
    max_length = 0

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # Calculate the length of the line
        line_length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Update if this line is the longest
        if line_length > max_length:
            max_length = line_length
            longest_line = (x1, y1, x2, y2)

        # Optionally, draw all lines for visualization
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw lines in blue

    if longest_line is None:
        raise ValueError("No suitable lines detected")

    # Draw the longest line in red for visualization
    x1, y1, x2, y2 = longest_line
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)  # Draw the longest line in red
    
    # Calculate the angle of the longest line with respect to the horizontal axis
    angle_radians = np.arctan2(y2 - y1, x2 - x1)  # Angle in radians
    angle_degrees = np.degrees(angle_radians)  # Convert to degrees

    # Normalize the angle to be between 0 and 360 degrees
    if angle_degrees < 0:
        angle_degrees += 360

    # Show the image with lines drawn
    cv2.imshow('Detected Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the coordinates of the longest line
    return longest_line, angle_degrees
