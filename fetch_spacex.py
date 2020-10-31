import requests
import os
import save_image

def getrocketsimages(url, path):
  response = requests.get(url)
  images_folder = response.json[100]['links']['flickr_images']
  response.raise_for_status()

  for index in image_folder:
    os.makedirs(path, exist_ok=True)
    save_image.saveimage(path, images_folder[index], f'rocket{index}.jpg')