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


bot = Bot()

def find_format(image_name):
  return os.path.splitext(image_name)[-1]

def downloadimage(url, image_id):
    path = 'images/'
    filename = f'{image_id}.jpg'
    response = requests.get(url)
    last_image_url = response.json()['image_files'][-1]['file_url']
    url = f"https://{urlparse(last_image_url).netloc}{urlparse(last_image_url).path}"
    
    os.makedirs(path, exist_ok=True)
    save_image.saveimage(path, url, filename)
 
def resizeimage(image_id, size1, size2):
    image = Image.open(f"images/{image_id}.jpg")
    image.thumbnail((size1, size2))
    image.save(f"images/{image_id}.jpg")

if __name__ == "__main__":
    bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'), proxy=None)

    first_image_id = 3815
    last_image_id = 4747

    url = 'https://api.spacexdata.com/v3/launches'
    sec_url = 'http://hubblesite.org/api/v3/image/'
    
    path = 'images/'
    
    descriptions = ["Nice picture!", "Very Intresting!", "So Cool!", "Very beautifull landscape!", "OMG!", "Nice pic!", "No words only emotions"]

    for image_id in range(first_image_id, last_image_id):
        try:
          resizeimage(image_id, 1080, 1080)
          bot.upload_photo(f"images/{image_id}.jpg", caption=random.choice(descriptions))
        except FileNotFoundError:
          logging.error(f"фотография {image_id} не найдена")