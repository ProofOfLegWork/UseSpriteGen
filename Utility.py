# From the folders, we can use the images to create sprite sheets.
import os
import re
import shutil

# Path to the Images folder
images_folder = "Images"
import sys
small_images_folder = "SmallImages"

os.makedirs(small_images_folder, exist_ok=True)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from SpriteGeneratorLibrary.GenerateSmallerImages import split_image_by_empty_space
except ModuleNotFoundError:
    print("Error: Could not resolve 'SpriteGeneratorLibrary.GenerateSmallerImages'. Please check the module path.")
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
                        split_image_by_empty_space(image_path, small_folder_path, folder_name)
                        
                        # # Save the smaller images in the corresponding SmallImages folder
                        # for idx, small_image in enumerate(smaller_images):
                        #     small_image_path = os.path.join(small_folder_path, f"{os.path.splitext(image_file)[0]}_{idx}.png")
                        #     small_image.save(small_image_path)
                        #     print(f"Saved: {small_image_path}")
                    except Exception as e:
                        print(f"Error processing {image_file} in {folder_name}: {e}")

# Call the function
def process_images_in_folder(images_folder, small_images_folder, image_name):            
    # Check if it's a directory
    if os.path.isdir(images_folder):

        # Process each image in the folder
        for image_file in os.listdir(images_folder):
            image_path = os.path.join(images_folder, image_file)
            
            # Check if it's a valid image file
            if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Split the image into smaller images
                    split_image_by_empty_space(image_path, small_images_folder, image_name)
                    
            
                except Exception as e:
                    print(f"Error processing {image_file} in {image_name}: {e}")


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


def delete_folders_with_one_image(small_images_folder):
    # Iterate through each folder inside SmallImages
    for folder_name in os.listdir(small_images_folder):
        folder_path = os.path.join(small_images_folder, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Count the number of image files in the folder
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            # If the folder contains only one image, delete the folder
            if len(image_files) == 1:
                try:
                    # Delete the folder and its contents
                    for file in image_files:
                        os.remove(os.path.join(folder_path, file))
                    os.rmdir(folder_path)
                    print(f"Deleted folder: {folder_path}")
                except Exception as e:
                    print(f"Error deleting folder {folder_path}: {e}")

# Call the function
#delete_folders_with_one_image(small_images_folder)
def ensure_directory_exists(directory_path):
    """Create the directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory ensured: {directory_path}")

# Example usage

def create_fuzzy_image(image_folder, output_path):
    """Blend multiple images together to create a fuzzy effect."""
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("No valid images found in the folder.")
        return

    # Open the first image to initialize the blending process
    base_image = None
    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(image_folder, image_file)
        try:
            with Image.open(image_path) as img:
                img = img.convert("RGBA")  # Ensure all images have the same mode
                if base_image is None:
                    base_image = img
                else:
                    # Blend the current image with the base image
                    base_image = Image.blend(base_image, img, alpha=1/(idx + 2))  # Gradually reduce the weight of each image
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    if base_image:
        # Save the resulting fuzzy image
        base_image.save(output_path)
        print(f"Fuzzy image saved to: {output_path}")
    else:
        print("No images were processed.")

#create_fuzzy_image("SmallImages/Mounts", "./fuzzy_image.png")


# Call the function for the Images folder
#rename_folders_in_directory(images_folder)
images_folder = "Locations"
small_images_folder = "SmallLocations"

#ensure_directory_exists(small_images_folder)
def clear_all_folders_inside(folder_path):
    """Delete all contents of folders inside the specified folder."""
    for folder_name in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_full_path):
            try:
                # Delete the folder and its contents
                shutil.rmtree(folder_full_path)
                print(f"Cleared folder: {folder_full_path}")
            except Exception as e:
                print(f"Error clearing folder {folder_full_path}: {e}")

# clear_all_folders_inside(small_images_folder)

# process_images_in_folders(images_folder, small_images_folder)
# #resize_images_with_background(small_images_folder)
# resize_images_with_background_no_ar(small_images_folder)
# delete_folders_with_one_image(small_images_folder)


# for folder_name in os.listdir(images_folder):
#          folder_path = os.path.join(small_images_folder, folder_name)
#          remove_small_images(folder_path)

def create_directory_and_copy_file(destination_directory, file_to_copy, smallImagesFolder):
    """Create a new directory under the specified directory and copy a file to it."""
    new_directory = os.path.join(destination_directory, smallImagesFolder)
    os.makedirs(new_directory, exist_ok=True)
    print(f"Directory created: {new_directory}")
    
    try:
        shutil.copy(file_to_copy, destination_directory)
        print(f"File copied to: {destination_directory}")
    except Exception as e:
        print(f"Error copying file: {e}")
    return new_directory


from datetime import datetime
def SingleImageProcessor(image_path, image_name):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_folder = f"OneImagePorcessor_{current_time}"    
    #image_path = r'C:\Users\parag-network\OneDrive\One notes\polw\allsmlogo.jpg'
    os.makedirs(output_folder, exist_ok=True)
    
    #image = Image.open(image_path)
    smallImagefolder = "SmallImagesFolder"
    
    newdir = create_directory_and_copy_file(output_folder, image_path, smallImagefolder)
    process_images_in_folder(output_folder, newdir, image_name)

def make_transparent(input_path, output_path, color_to_make_transparent=(255, 255, 255)):
    """
    Make the specified color in an image transparent.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the output image.
        color_to_make_transparent (tuple): RGB color to make transparent (default is white).
    """
    try:
        # Open the image
        img = Image.open(input_path).convert("RGBA")

        # Get the image data
        data = img.getdata()

        # Create a new data list with transparency applied
        new_data = []
        for item in data:
            # Check if the pixel matches the color to make transparent
            if item[:3] == color_to_make_transparent:
                # Make the pixel fully transparent
                new_data.append((255, 255, 255, 0))
            else:
                # Keep the pixel as is
                new_data.append(item)

        # Update the image data
        img.putdata(new_data)

        # Save the new image
        img.save(output_path, "PNG")
        print(f"✅ Transparent image saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error processing the image: {e}")

# Example usage
# input_image = "path/to/your/image.jpg"  # Replace with your input image path
# output_image = "path/to/your/output_image.png"  # Replace with your desired output path
# make_transparent(input_image, output_image)
def CreateDirectoryAndTransparentAllImages(folder_path, small_image_folder):
    input_folder = os.path.join(folder_path, small_image_folder)  
    output_folder = os.path.join(folder_path, "TransparentImages")
    os.makedirs(output_folder, exist_ok=True)
    #image_path = r'C:\Users\parag-network\OneDrive\One notes\polw\allsmlogo.jpg'
    for image_file in os.listdir(input_folder):
        input_path = os.path.join(input_folder, image_file)
        if os.path.isfile(input_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path = os.path.join(output_folder, f"transparent_{image_file}")
            make_transparent(input_path, output_path)

# Example usage
# destination_directory = "OutputDirectory"
file_to_copy = r'/home/parag/all-code/UseSpriteGen/Poison/Poison_bottles/generated_image.png'
#create_directory_and_copy_file(destination_directory, file_to_copy)
SingleImageProcessor(file_to_copy, "Poison")


#CreateDirectoryAndTransparentAllImages("Poison", "SmallImages")