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
import save_images

bot = Bot()

def find_format(image_name):
  return ((image_name.replace('.', ' ')).split())[-1]

def DownloadImage(url, image_id):
  path = 'images/'
  filename = f'{image_id}.jpg'
  response = requests.get(url)
  last_image_url = response.json()['image_files'][-1]['file_url']
  url = f"https://{urlparse(last_image_url).netloc}{urlparse(last_image_url).path}"
  
  save_images.SaveImages(path, url, filename)

def DownloadImageCollection(url):
    collections = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
      response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
      for index in response.json():
          DownloadImage(f"{url}{index['id']}" , index['id'])   

def ResizeImage(image_id, size1, size2):
  image = Image.open(f"images/{image_id}.jpg")
  image.thumbnail((size1, size2))
  image.save(f"images/{image_id}.jpg")

def UploadPhoto(image_id, caption):
  bot.upload_photo(f"images/{image_id}.jpg", caption=caption)

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
      ResizeImage(image_id, 1080, 1080)
      UploadPhoto(image_id, random.choice(descriptions))
    except FileNotFoundError:
      logging.error(f"фотография {image_id} не найдена")