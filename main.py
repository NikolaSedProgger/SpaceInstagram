import requests
import os
import pathlib
import json
import itertools
from urllib.parse import urlparse
from PIL import Image
from instabot import Bot
import random 
import logging
import save_image
import argparse

def download_image(url, image_id):
    path = 'images/'
    filename = f'{image_id}.jpg'
    response = requests.get(url)
    last_image_url = response.json()['image_files'][-1]['file_url']
    url = f"https://{urlparse(last_image_url).netloc}{urlparse(last_image_url).path}"
    
    os.makedirs(path, exist_ok=True)
    save_image.save_image(path, url, filename)
 
def resize_image(image_id, size1, size2):
    image = Image.open(f"images/{image_id}.jpg")
    image.thumbnail((size1, size2))
    image.save(f"images/{image_id}.jpg")

if __name__ == "__main__":
    bot = Bot()
    
    bot.login(username=os.getenv('BITLY_LOGIN'), password=os.getenv('BITLY_PASSWORD'), proxy=None)

    first_image_id = 3961
    last_image_id = 4747
    
    descriptions = ["Nice picture!", "Very Intresting!", "So Cool!", "Very beautifull landscape!", "OMG!", "Nice pic!", "No words only emotions"]

    for image_id in range(first_image_id, last_image_id):
        try:
            resize_image(image_id, 1080, 1080)
            raise ValueError()
            bot.upload_photo(f"images/{image_id}.jpg", caption=random.choice(descriptions))
        except FileNotFoundError:
            logging.error(f"фотография {image_id} не найдена")
        finally:
            try:
                removal_image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images', f'{image_id}.jpg')
                os.remove(removal_image_path)
            except FileNotFoundError:
                print(f'{image_id}.jpg не найдено')