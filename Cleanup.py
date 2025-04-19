import os
import shutil

def delete_downloads_folders(base_directory):
    """Remove all folders starting with 'Downloads_' in the specified directory."""
    for folder_name in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder_name)
        
        # Check if it's a directory and starts with 'Downloads_'
        if os.path.isdir(folder_path) and folder_name.startswith("Downloads_"):
            try:
                shutil.rmtree(folder_path)  # Remove the folder and its contents
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                print(f"Error deleting folder {folder_path}: {e}")

# Example usage
base_directory = "."  # Replace with the path to your base directory
delete_downloads_folders(base_directory)