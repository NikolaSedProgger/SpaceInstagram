import requests
import json
import os

def SaveImages(path, url, name):
  os.makedirs(path, exist_ok=True)

  response = requests.get(url, verify=False)
  response.raise_for_status()

  image_path = os.path.join(path, name)
  with open(image_path, 'wb') as file:
    file.write(response.content)

def GetRocketsImages(url, path, images_range):
  response = requests.get(url)
  image_dictionary = json.loads(response.content)[100]['links']['flickr_images']
  response.raise_for_status()

  for index in range(images_range):
    SaveImages(path, image_dictionary[index], f'rocket{index}.jpg')