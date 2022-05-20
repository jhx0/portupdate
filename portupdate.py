#!/usr/bin/env python3

import re
import emoji
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# the URL should not be changed
url = 'https://www.freshports.org/'

# max number of port updates to show
# tune this to your needs
max_updates = 10

def showUpdates():
    init()

    data = requests.get(url)

    html = BeautifulSoup(data.text, 'html.parser')

    count = 0

    for item in html.find_all('span', { 'class': 'element-details' }):
        if count >= max_updates:
            break

        name, version = item.text.split(" ")
        print("{} {: <50}{}".format(emoji.emojize(':package:'),
                                Fore.GREEN + Style.BRIGHT + name, 
                                Fore.RED + Style.BRIGHT + version))
        count += 1 

def main():
    showUpdates()

if __name__ == "__main__":
    main()
