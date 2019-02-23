#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.freshports.org/'

def showUpdates():
    data = requests.get(url)

    html = BeautifulSoup(data.text, 'html.parser')

    regexp = re.compile(r'href=*')

    for item in html.select('big > b'):
        if not regexp.search(str(item)):
            continue

        name, version = item.text.split(" ")
        print("{: <50}{}".format(name, version))

if __name__ == "__main__":
    showUpdates()
