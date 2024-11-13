from angle_detection import detect_longest_line

def compare_clock_hands(image_path1, image_path2):
    # Detect the longest line (minute hand) and angle in both images
    longest_line1, angle1 = detect_longest_line(image_path1)
    longest_line2, angle2 = detect_longest_line(image_path2)

    # Print the angles detected
    print(f"Angle of minute hand in first image: {angle1:.2f} degrees")
    print(f"Angle of minute hand in second image: {angle2:.2f} degrees")

    # Calculate the absolute difference between the two angles
    angle_difference = abs(angle1 - angle2)

    # Ensure the angle difference is within 0-180 degrees
    if angle_difference > 180:
        angle_difference = 360 - angle_difference

    # Print and return the angle difference between the minute hands
    print(f"The angle difference between the minute hands is: {angle_difference:.2f} degrees")
    return angle_difference

