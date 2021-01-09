import requests
import os
from main import download_image

def download_images_collections(url):
    collections = ["holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"]
    for collection in collections:
        get_hubble_images(collection, url)
        
def get_hubble_images(collection, url):
    response = requests.get(f"http://hubblesite.org/api/v3/images/{collection}")
    response.raise_for_status()
    for image in response.json():
        download_image(f"{url}{image['id']}", image['id']) 


if __name__ == "__main__":
    second_url = 'http://hubblesite.org/api/v3/image/'
    download_images_collections(second_url)
