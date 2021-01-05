import requests
import os
import save_image




def get_rockets_images(url, path):
    images_links_index = 100
    response = requests.get(url)
    response.raise_for_status()
    
    images_folder = response.json()[images_links_index]['links']['flickr_images']
    image_num = 1

    for index, image_num in enumerate(images_folder):
        os.makedirs(path, exist_ok=True)
        save_image.save_image(path, index, f'rocket{image_num}.jpg')

if __name__ == "__main__":
    url = 'https://api.spacexdata.com/v3/launches'
    path = 'images/'
    
    get_rockets_images(url, path)