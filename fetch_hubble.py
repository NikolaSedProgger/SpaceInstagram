import requests
from save_image import save_image
from urllib.parse import urlparse
import os

def download_image(url, image_id, path):
    filename = f'{image_id}.jpg'
    response = requests.get(url)
    response.raise_for_status()

    last_image_url = response.json()['image_files'][-1]['file_url']
    parsed_image_url = urlparse(last_image_url)
    url = f"https://{parsed_image_url.netloc}{parsed_image_url.path}"
    save_image(path, url, filename)


def download_images_collections(url):
    collections = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
        get_hubble_images(collection, url)


def get_hubble_images(collection, url):
    response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
    response.raise_for_status()
    for image in response.json():
        download_image(f"{url}{image['id']}", image['id'], path)


if __name__ == "__main__":
    second_url = 'http://hubblesite.org/api/v3/image/'
    download_images_collections(second_url)
    path = os.path.join("images")