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

def GetHubbleImages(url, image_range, path):
  response = requests.get(url)
  images = json.loads(response.content)['image_files']
  images_list = []
  for index in range(image_range):
    images_list.append(images[index]['file_url'])