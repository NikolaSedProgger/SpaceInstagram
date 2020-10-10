import requests
import os
import pathlib
import json
import itertools
from urllib.parse import urlparse
from PIL import Image
from instabot import Bot
import random 

def SaveImages(path, url, name):
  os.makedirs(path, exist_ok=True)

  response = requests.get(url, verify=False)
  response.raise_for_status()

  image_path = os.path.join(path, name)
  with open(image_path, 'wb') as file:
    file.write(response.content)

def split_format(image_name):
  return ((image_name.replace('.', ' ')).split())[-1]

def DownloadImage(url, id):
  path = 'images/'
  filename = f'{id}.jpg'
  response = requests.get(url)
  last_image_url = response.json()['image_files'][-1]['file_url']
  url = f"https://{urlparse(last_image_url).netloc}{urlparse(last_image_url).path}"
  
  SaveImages(path, url, filename)

def DownloadImageCollection(url):
    collections = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
      response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
      print(f"На данный момент скачиваются картинки из коллекции {collection}")
      for index in response.json():
          images_response = requests.get(f"{url}{index['id']}")
          DownloadImage(f"{url}{index['id']}" , index['id'])
          print(f"Картинка {index['id']}.jpg успешно загружена")   

def ResizeImage(image_id, size1, size2):
  image = Image.open(f"images/{image_id}.jpg")
  image.thumbnail((size1, size2))
  image.save(f"images/{image_id}.jpg")

def UploadPhoto(image_id, caption):
  bot.upload_photo(f"images/{image_id}.jpg", caption=caption)

if __name__ == "__main__":
  bot = Bot()
  bot.login(username=os.getenv('LOGIN'), password=os.getenv('PASSWORD'), proxy=None)

  url = 'https://api.spacexdata.com/v3/launches'
  sec_url = 'http://hubblesite.org/api/v3/image/'
  
  path = 'images/'
  
  descriptions = ["Nice picture!", "Very Intresting!", "So Cool!", "Very beautifull landscape!", "OMG!", "Nice pic!", "No words only emotions"]

  for image_id in range(3815, 4747):
    try:
      ResizeImage(image_id, 1080, 1080)
      UploadPhoto(image_id, random.choice(descriptions))
    except FileNotFoundError:
      print(f"изображение {image_id}.jpg не найдено")