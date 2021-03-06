import os
from instabot import Bot
from PIL import Image
import random
import logging


def resize_image(image_id, width, height, path):
    image = Image.open(f"{path}/{image_id}.jpg")
    image.thumbnail((width, height))
    image.save(f"{path}/{image_id}.jpg")

if __name__ == "__main__":
    bot = Bot()
    login = os.getenv('BITLY_LOGIN')
    password = os.getenv('BITLY_PASSWORD')
    bot.login(username=login, password=password, proxy=None)

    path = os.path.join(os.path.sep, 'images')
    width = 1080
    height = 1080
    os.makedirs(path, exist_ok=True)

    first_image_id = os.path.splitext(os.listdir(path)[0])[0]
    last_image_id = os.path.splitext(os.listdir(path)[-1])[0]

    descriptions = ["Nice picture!", "Very beautifull landscape!", "OMG!"]

    for image_id in range(first_image_id, last_image_id):
        try:
            resize_image(image_id, width, height, path)
            bot.upload_photo(f"{path}/{image_id}.jpg", caption=random.choice(descriptions))
        except FileNotFoundError:
            logging.error(f"фотография {image_id} не найдена")
        finally:
            try:
                removal_image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path, f'{image_id}.jpg')
                os.remove(removal_image_path)
            except FileNotFoundError:
                print(f'{image_id}.jpg не найдено')
