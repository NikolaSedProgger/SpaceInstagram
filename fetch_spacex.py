import requests
import json
import os
import save_image

def getrocketsimages(url, path, images_range):
  response = requests.get(url)
  image_dictionary = json.loads(response.content)[100]['links']['flickr_images']
  response.raise_for_status()

  for index in range(images_range):
    os.makedirs(path, exist_ok=True)
    save_image.saveimage(path, image_dictionary[index], f'rocket{index}.jpg')