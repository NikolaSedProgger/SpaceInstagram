import requests
import json
import os
import save_images

def GetRocketsImages(url, path, images_range):
  response = requests.get(url)
  image_dictionary = json.loads(response.content)[100]['links']['flickr_images']
  response.raise_for_status()

  for index in range(images_range):
    save_images.SaveImages(path, image_dictionary[index], f'rocket{index}.jpg')