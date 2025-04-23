import os
from PIL import Image
from datetime import datetime

def split_sprite_sheet(
    sprite_sheet_path, 
    output_folder, 
    sprite_width, 
    sprite_height, 
    columns=None, 
    rows=None, 
    padding=0, 
    margin=0
):
    """
    Split a sprite sheet into individual sprite images.
    
    Args:
        sprite_sheet_path (str): Path to the sprite sheet image
        output_folder (str): Folder to save the individual sprites
        sprite_width (int): Width of each sprite in pixels
        sprite_height (int): Height of each sprite in pixels
        columns (int, optional): Number of columns in the sprite sheet. If None, calculated from image width.
        rows (int, optional): Number of rows in the sprite sheet. If None, calculated from image height.
        padding (int, optional): Padding between sprites in pixels
        margin (int, optional): Margin around the sprite sheet in pixels
    
    Returns:
        int: Number of sprites extracted
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the sprite sheet
    try:
        sprite_sheet = Image.open(sprite_sheet_path)
    except Exception as e:
        print(f"Error opening sprite sheet: {e}")
        return 0
    
    # Get sprite sheet dimensions
    sheet_width, sheet_height = sprite_sheet.size
    
    # Calculate number of columns and rows if not provided
    if columns is None:
        columns = (sheet_width - 2 * margin + padding) // (sprite_width + padding)
    
    if rows is None:
        rows = (sheet_height - 2 * margin + padding) // (sprite_height + padding)
    
    print(f"Splitting sprite sheet into {columns}x{rows} grid ({columns * rows} sprites)")
    
    # Extract each sprite
    sprite_count = 0
    for row in range(rows):
        for col in range(columns):
            # Calculate sprite position
            x = margin + col * (sprite_width + padding)
            y = margin + row * (sprite_height + padding)
            
            # Check if we're still within the image bounds
            if x + sprite_width <= sheet_width and y + sprite_height <= sheet_height:
                # Extract the sprite
                sprite = sprite_sheet.crop((x, y, x + sprite_width, y + sprite_height))
                
                # Save the sprite
                sprite_filename = f"sprite_{sprite_count:03d}.png"
                sprite_path = os.path.join(output_folder, sprite_filename)
                sprite.save(sprite_path)
                print(f"Saved sprite to {sprite_path}")
                
                sprite_count += 1
    
    print(f"Successfully extracted {sprite_count} sprites from {sprite_sheet_path}")
    return sprite_count


def auto_detect_sprite_size(sprite_sheet_path, min_size=8, max_size=128):
    """
    Attempt to automatically detect sprite size in a sprite sheet.
    This is a simple implementation that looks for repeating patterns.
    
    Args:
        sprite_sheet_path (str): Path to the sprite sheet image
        min_size (int): Minimum sprite size to consider
        max_size (int): Maximum sprite size to consider
        
    Returns:
        tuple: (width, height) of detected sprite size, or None if detection fails
    """
    try:
        sprite_sheet = Image.open(sprite_sheet_path).convert("RGBA")
        width, height = sprite_sheet.size
        
        # Try to detect horizontal sprite width
        for test_width in range(min_size, min(width // 2, max_size)):
            column_similar = True
            for x in range(0, width - test_width, test_width):
                col1 = [sprite_sheet.getpixel((x, y)) for y in range(height)]
                col2 = [sprite_sheet.getpixel((x + test_width, y)) for y in range(height)]
                if col1 != col2:
                    column_similar = False
                    break
            
            if column_similar:
                # Try to detect vertical sprite height
                for test_height in range(min_size, min(height // 2, max_size)):
                    row_similar = True
                    for y in range(0, height - test_height, test_height):
                        row1 = [sprite_sheet.getpixel((x, y)) for x in range(width)]
                        row2 = [sprite_sheet.getpixel((x, y + test_height)) for x in range(width)]
                        if row1 != row2:
                            row_similar = False
                            break
                    
                    if row_similar:
                        return (test_width, test_height)
        
        return None
    except Exception as e:
        print(f"Error detecting sprite size: {e}")
        return None
    
output_folder = "output_sprites"
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folder = f"OneImagePorcessor_{output_folder}_{current_time}"
split_sprite_sheet('/home/parag/all-code/UseSpriteGen/OneImagePorcessor_2025-04-23_13-48-23/generated_image.png', output_folder, 256, 256, padding=2, margin=2)
# Example usage
#split_sprite_sheet('POison')