import requests
import json
import os
import save_images

def GetHubbleImages(url, image_range, path):
  response = requests.get(url)
  get_images = json.loads(response.content)['image_files']
  images = []
  for index in get_images:
    images.append(images[index]['file_url'])

