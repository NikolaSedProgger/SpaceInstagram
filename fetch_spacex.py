import requests
import os
import save_image




def get_rockets_images(url, path):
  images_links_index = 100
  response = requests.get(url)
  images_folder = response.json()[images_links_index]['links']['flickr_images']
  response.raise_for_status()
  image_num = 1

  for index in images_folder:
    os.makedirs(path, exist_ok=True)
    print(index)
    print(image_num)
    save_image.saveimage(path, index, f'rocket{image_num}.jpg')
    image_num = image_num + 1

if __name__ == "__main__":
  url = 'https://api.spacexdata.com/v3/launches'
  path = 'images/'
  
  get_rockets_images(url, path)