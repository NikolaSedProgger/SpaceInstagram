import os
import requests

def saveimage(path, url, name):
  response = requests.get(url, verify=False)
  response.raise_for_status()

  image_path = os.path.join(path, name)
  
  with open(image_path, 'wb') as file:
    file.write(response.content)