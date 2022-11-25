import logging
import os
import requests

logging.basicConfig(level=logging.INFO)

class XmlHandler:
  @staticmethod
  def download(url: str) -> str:
    logging.info(f"downloading file {url}...")
    filename: str = get_filename_from_url(url)
    response = requests.get(url)
    with open(f"temp/{filename}", 'wb') as file:
        file.write(response.content)
    return filename

  @staticmethod
  def delete(filename: str):
    logging.info(f"Deleting file {filename}...")
    os.remove(f"temp/{filename}")


def get_filename_from_url(url: str) -> str:
  return url.split("/")[-1]