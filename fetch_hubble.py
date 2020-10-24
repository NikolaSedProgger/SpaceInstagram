import requests
import os
import save_image

def gethubbleimages(url, image_range, path):
  response = requests.get(url)
  get_images = response.json['image_files']
  images = []
  for index in get_images:
    images.append(images[index]['file_url'])

