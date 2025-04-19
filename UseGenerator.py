import openai
import os
import requests
from datetime import datetime

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

categories = [
    "Medical professionals",
    "Positive Fictional characters",
    "Negative Fictional characters",
    "Villains",
    "Heroes",
    "Weapons",
    "Knives",
    "Swords",
    "Shields",
    "Armors",
    "Horses",
    "Mounts",
    "Monsters",
    "Dragons",
    "Mythical creatures",
    "Animals",
    "Birds",        
    "Fish",
    "Reptiles",
    "Insects",
    "Plants",
    "Trees",
    "Flowers",
    "Crops",
    "Fruits",
    "Vegetables",
    "Buildings",
    "Castles",
    "Towers",
    "Bridges",
    "Roads",
    "Vehicles",
    "Cars"
]

# Iterate over each category
for category_name in categories:
    try:
        # Generate the image using DALL-E
        response = openai.images.generate(
            model="dall-e-3",
            prompt=f"A retro pixel art sprite sheet of {category_name}",
            n=1,
            size="1024x1024"
        )

        # Get the image URL
        image_url = response.data[0].url
        print(f"🔗 Image URL for {category_name}: {image_url}")

        # Create a folder with a timestamp for the category
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_folder = f"{category_name.replace(' ', '_')}_{timestamp}"
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