import requests
import os
import save_image




def getrocketsimages(url, path):
  response = requests.get(url)
  images_folder = response.json[100]['links']['flickr_images']
  response.raise_for_status()

  for index in images_folder:
    os.makedirs(path, exist_ok=True)
    save_image.saveimage(path, images_folder[index], f'rocket{index}.jpg')

if __name__ == "__main__":
  url = 'https://api.spacexdata.com/v3/launches'
  path = 'images/'
  
  getrocketsimages(url, path)