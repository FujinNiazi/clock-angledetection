# detect_edges.py
from compare_hands import compare_clock_hands

# Define the paths to your two clock images
image_path1 = 'clock1.jpg'
image_path2 = 'clock2.png'

# Modify this variable to 'hour' or 'minute' based on which hand you want to compare
hand_type = 'minute'  # Change to 'minute' if you want to compare minute hands

# Step 1: Compare the selected hands of the two clock images
compare_clock_hands(image_path1, image_path2, hand_type=hand_type)
