# From the folders, we can use the images to create sprite sheets.
import os
import re

# Path to the Images folder
images_folder = "Images"
import sys
small_images_folder = "SmallImages"

os.makedirs(small_images_folder, exist_ok=True)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from SpriteGeneratorLibrary.GenerateSmallerImages import split_image_by_empty_space
except ModuleNotFoundError:
    print("Error: Could not resolve 'SpriteSheetGenerator.GenerateSmallerImages'. Please check the module path.")
    split_image_by_empty_space = None
from SpriteGeneratorLibrary.Resize_withAndWithoutAspect import resize_images_to_fixed_size, resize_images_with_background_no_ar, resize_images_with_background
from PIL import Image
from SpriteGeneratorLibrary.RemoveSmallImages import remove_small_images

def process_images_in_folders(images_folder, small_images_folder):
    for folder_name in os.listdir(images_folder):
        folder_path = os.path.join(images_folder, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Create a corresponding folder in SmallImages
            small_folder_path = os.path.join(small_images_folder, folder_name)
            os.makedirs(small_folder_path, exist_ok=True)

            # Process each image in the folder
            for image_file in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_file)
                
                # Check if it's a valid image file
                if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        # Split the image into smaller images
                        split_image_by_empty_space(image_path, small_folder_path)
                        
                        # # Save the smaller images in the corresponding SmallImages folder
                        # for idx, small_image in enumerate(smaller_images):
                        #     small_image_path = os.path.join(small_folder_path, f"{os.path.splitext(image_file)[0]}_{idx}.png")
                        #     small_image.save(small_image_path)
                        #     print(f"Saved: {small_image_path}")
                    except Exception as e:
                        print(f"Error processing {image_file} in {folder_name}: {e}")

# Call the function



# Add the directory two levels up to the Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../SpriteSheetGenerator")))

# Now you can import UseGenerator
# Iterate through each folder inside the Images folder
def rename_folders_in_directory(directory):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Remove numbers and underscores from the folder name
            new_folder_name = re.sub(r'[0-9_]', '', folder_name)
            new_folder_path = os.path.join(directory, new_folder_name)
            
            # Rename the folder
            os.rename(folder_path, new_folder_path)
            print(f"Renamed: {folder_name} -> {new_folder_name}")

# Call the function for the Images folder
#rename_folders_in_directory(images_folder)

#process_images_in_folders(images_folder, small_images_folder)
#resize_images_with_background(small_images_folder)
#resize_images_with_background_no_ar(small_images_folder)
for folder_name in os.listdir(images_folder):
        folder_path = os.path.join(small_images_folder, folder_name)
        remove_small_images(folder_path)