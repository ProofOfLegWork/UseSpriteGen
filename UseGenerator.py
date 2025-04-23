import openai
"""
UseGenerator.py

This script generates retro pixel art sprite sheets for various categories using OpenAI's DALL-E model. 
The generated images are downloaded and saved into timestamped folders for each category.

Modules:
    - openai: Used to interact with OpenAI's API for generating images.
    - os: Provides functions for interacting with the operating system, such as creating directories.
    - requests: Used to make HTTP requests for downloading images.
    - datetime: Provides functions to work with dates and times.

Constants:
    - categories (list): A list of categories for which sprite sheets will be generated.

Workflow:
    1. Iterate over each category in the `categories` list.
    2. Generate an image using the DALL-E model with a prompt specific to the category.
    3. Retrieve the image URL from the API response.
    4. Create a timestamped folder for the category to store the downloaded image.
    5. Download the image from the URL and save it to the folder.
    6. Handle any errors that occur during the process and log appropriate messages.

Error Handling:
    - Catches exceptions during the image generation and download process.
    - Logs errors with the category name and exception details.

Usage:
    - Replace "YOUR_API_KEY" with your OpenAI API key before running the script.
    - Run the script to generate and download sprite sheets for all categories in the list.

Example:
    To generate a sprite sheet for "Medical professionals", the script will:
    - Send a prompt to the DALL-E model.
    - Create a folder named "Medical_professionals_<timestamp>".
    - Download the generated image into the folder as "generated_image.png".

Notes:
    - Ensure you have an active OpenAI API key and internet connection.
    - The script uses the DALL-E model version "dall-e-3".
    - The generated images are in 1024x1024 resolution.

Comments:
    - Inline comments are added throughout the script to explain each step of the process.
    - These comments provide clarity on the purpose and functionality of each code block.
"""
import os
import requests
from datetime import datetime

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

categories= [
    "Libraries",
    "Schools",
    "Hospitals",
    "Police Stations",
    "Fire Stations",
    "Courthouses",
    "Banks",
    "Post Offices",
    "Government Buildings",
    "Courthouses",
    "Houses",
    "Studyrooms",
    "Living Rooms",
    "Bedrooms",
    "Bathrooms"
 ]


# categories = [

#     "Knives",
#     "Swords",
#     "Shields",
#     "Armors",
#     "Poisons",
#     "Revolvers",
#     "Pistols",
#     "Axe",
#     "Spears",
#     "Bows",
#     "Crossbows",
#     "Clubs/bats",
#     "Maces"
# ]
# categories = [
#     "Medical professionals",
#     "Positive Fictional characters",
#     "Negative Fictional characters",
#     "Villains",
#     "Heroes",
#     "Weapons",
#     "Knives",
#     "Swords",
#     "Shields",
#     "Armors",
#     "Horses",
#     "Mounts",
#     "Monsters",
#     "Dragons",
#     "Mythical creatures",
#     "Animals",
#     "Birds",        
#     "Fish",
#     "Reptiles",
#     "Insects",
#     "Plants",
#     "Trees",
#     "Flowers",
#     "Crops",
#     "Fruits",
#     "Vegetables",
#     "Buildings",
#     "Castles",
#     "Towers",
#     "Bridges",
#     "Roads",
#     "Vehicles",
#     "Cars"
# ]

# Iterate over each category

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folder = f"Downloads_{current_time}"
os.makedirs(output_folder, exist_ok=True)

for category_name in categories:
    try:
        # Generate the image using DALL-E
        # response = openai.images.generate(
        #     model="dall-e-3",
        #     prompt=f"A image of {category_name} in madhubani style",
        #     n=1,
        #     size="256x256"
        # )

        response = openai.images.generate(
            model="dall-e-3",
            prompt=f"A retro pixel art sprite sheet of {category_name}",
            n=1,
            size="1792x1024"
        )
         
        # Get the image URL
        image_url = response.data[0].url
        print(f"🔗 Image URL for {category_name}: {image_url}")

        # Create a folder with a timestamp for the category
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_folder = os.path.join(output_folder, f"{category_name.replace(' ', '_')}")
        os.makedirs(download_folder, exist_ok=True)

        # Download the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_path = os.path.join(download_folder, "generated_image.png")
            with open(image_path, "wb") as f:
                f.write(image_response.content)
            print(f"✅ Image for {category_name} downloaded to: {image_path}")
        else:
            print(f"❌ Failed to download the image for {category_name}.")
    except Exception as e:
        print(f"❌ Error processing category {category_name}: {e}")


    