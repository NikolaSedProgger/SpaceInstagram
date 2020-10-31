import requests
import os
import save_image

def gethubbleimages(url, path):
  response = requests.get(url)
  get_images = response.json['image_files']
  images = []
  for image in get_images:
    images.append(images[image]['file_url'])
  response.raise_for_status()

