# compare_hands.py
import cv2
import matplotlib.pyplot as plt
from angle_detection import detect_hour_hand, detect_minute_hand, calculate_angle_between_lines

# Function to compare clock hands between two images
def compare_clock_hands(image_path1, image_path2, hand_type="hour"):
    try:
        if hand_type == "hour":
            # Detect hour hand in both images
            image1, edges1, filtered_lines1, hand1 = detect_hour_hand(image_path1)
            image2, edges2, filtered_lines2, hand2 = detect_hour_hand(image_path2)
            hand_label = "Hour Hand"
        elif hand_type == "minute":
            # Detect minute hand in both images
            image1, edges1, filtered_lines1, hand1 = detect_minute_hand(image_path1)
            image2, edges2, filtered_lines2, hand2 = detect_minute_hand(image_path2)
            hand_label = "Minute Hand"
        else:
            raise ValueError(f"Invalid hand type: {hand_type}. Must be 'hour' or 'minute'.")

        # Extract the theta values (angles) of the hands
        theta1 = hand1[1]
        theta2 = hand2[1]

        # Calculate the angle between the two hands
        angle_between_hands = calculate_angle_between_lines(theta1, theta2)

        # Display results
        plt.figure(figsize=(15, 5))

        # First Image (with hand detected)
        plt.subplot(1, 3, 1)
        plt.imshow(image1, cmap='gray')
        plt.title(f"First Clock Image ({hand_label})")
        plt.axis('off')

        # Second Image (with hand detected)
        plt.subplot(1, 3, 2)
        plt.imshow(image2, cmap='gray')
        plt.title(f"Second Clock Image ({hand_label})")
        plt.axis('off')

        # Display the calculated angle
        plt.subplot(1, 3, 3)
        plt.text(0.5, 0.5, f"Angle Between {hand_label}s: {angle_between_hands:.2f}°", 
                 fontsize=16, ha='center', va='center')
        plt.axis('off')

        plt.show()

        # Print the angle between the hands
        print(f"Angle between the {hand_label}s: {angle_between_hands:.2f} degrees")

    except ValueError as e:
        print(e)
