from pathlib import Path
from compare_hands import compare_clock_hands

# Define the paths for the two input images
image_path1 = Path('data/images/clock1.jpg')  # Replace with the path to your first image
image_path2 = Path('data/images/clock3.jpg')  # Replace with the path to your second image

# Compare the minute hands and calculate the angle between them
compare_clock_hands(image_path1, image_path2)
