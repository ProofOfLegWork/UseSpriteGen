# From the folders, we can use the images to create sprite sheets.
import os
import re

# Path to the Images folder
images_folder = "Images"
import sys


# Add the directory two levels up to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../SpriteSheetGenerator")))

# Now you can import UseGenerator
import UseGenerator
# Iterate through each folder inside the Images folder
for folder_name in os.listdir(images_folder):
    folder_path = os.path.join(images_folder, folder_name)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Remove numbers and underscores from the folder name
        new_folder_name = re.sub(r'[0-9_]', '', folder_name)
        new_folder_path = os.path.join(images_folder, new_folder_name)
        
        # Rename the folder
        os.rename(folder_path, new_folder_path)
        print(f"Renamed: {folder_name} -> {new_folder_name}")