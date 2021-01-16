import requests
import os
from urllib.parse import urlparse
from instabot import Bot
from PIL import Image
import random
import logging
import save_image


def resize_image(image_id, width, height):
    image = Image.open(f"images/{image_id}.jpg")
    image.thumbnail((width, height))
    image.save(f"images/{image_id}.jpg")

if __name__ == "__main__":
    bot = Bot()
    login = os.getenv('BITLY_LOGIN')
    password = os.getenv('BITLY_PASSWORD')
    bot.login(username=login, password=password, proxy=None)

    path = "images/"
    os.makedirs(path, exist_ok=True)

    sorted_images_id = sorted(os.listdir(path))
    first_image_id = os.path.splitext(sorted_images_id[0])[0]
    last_image_id = os.path.splitext(sorted_images_id[-1])[0]

    descriptions = ["Nice picture!", "Very beautifull landscape!", "OMG!"]

    for image_id in range(first_image_id, last_image_id):
        try:
            resize_image(image_id, 1080, 1080)
            raise ValueError()
            bot.upload_photo(f"images/{image_id}.jpg", caption=random.choice(descriptions))
        except FileNotFoundError:
            logging.error(f"фотография {image_id} не найдена")
        finally:
            try:
                removal_image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images', f'{image_id}.jpg')
                os.remove(removal_image_path)
            except FileNotFoundError:
                print(f'{image_id}.jpg не найдено')
