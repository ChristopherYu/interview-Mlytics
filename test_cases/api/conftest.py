import os
import json

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def api_test_data() -> list:
    path = os.getcwd()
    with open(f"{path}/config/env.json", "r") as file:
        config = json.load(file)
        url = config["UAT"]["url"]
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.content, "html.parser")

        # find all tags of image
        img_tags = soup.find_all("img")
        urls = []
        # for img in img_tags:
        #     img_url = img.get("src")
        #     img_url = urljoin(url, img_url)
        #     urls.append(img_url)
        return urls
