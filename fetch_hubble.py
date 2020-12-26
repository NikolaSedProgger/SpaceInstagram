import requests
import os
import save_image
from main import downloadimage

def get_hubble_images(url, path):
  response = requests.get(url)
  get_images = response.json()['image_files']
  images = []
  for image in get_images:
    images.append(images[image]['file_url'])
  response.raise_for_status()

def download_image_collection(url):
    collections = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
      response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
      for element in response.json():
          downloadimage(f"{url}{element['id']}", element['id'])  


if __name__ == "__main__":
  sec_url = 'http://hubblesite.org/api/v3/image/'
  path = 'images/'

  download_image_collection(sec_url)