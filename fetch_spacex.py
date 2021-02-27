import requests
import os
import save_image


def get_rockets_images(url, path):
    images_links_index = 100
    response = requests.get(url)
    response.raise_for_status()
    images_links = response.json()[images_links_index]['links']
    flickr_images = images_links['flickr_images']
    for image_num, link in enumerate(flickr_images):
        save_image.save_image(path, link, f'{image_num}.jpg')


if __name__ == "__main__":
    url = 'https://api.spacexdata.com/v3/launches'
    path = os.path.join("images")
    os.makedirs(path, exist_ok=True)
    get_rockets_images(url, path)
