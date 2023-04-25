#!/usr/bin/env python

import requests
import os
import validators
from bs4 import BeautifulSoup
from urllib import (request, error, parse)
from urllib.request import (Request, urlopen)

HEADERS = {'Content-Type': 'text/html', 'User-Agent': 'Mozilla/5.0'}
OUTPUT_FILE = './downloaded_pages/'
LOGERROR = './log.error'

def download_webpage(url, num):
    try:
        req = Request(
            url=url, 
            headers=HEADERS
        )
        response = urlopen(req)

        #response = urllib.request.urlopen(url)
        webContent = response.read().decode(response.headers.get_content_charset())#.decode('UTF-8')

        f = open(os.path.join(OUTPUT_FILE, str(num)+'.txt'), 'w', encoding='UTF-8')
        f.write(webContent)
        f.close
    except Exception:
        with open(LOGERROR, 'a') as log_error:
            log_error.write(url + '\n')


def get_links(url):

    num = 0
    links = []
    website = requests.get(url, headers=HEADERS)
    website_text = website.text

    soup = BeautifulSoup(website_text, 'html.parser')

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    for link in links:

        if (str(link) != 'None'):
            if validators.url(url + '/' + link):
                download_webpage(url + '/' + link, num)
                num += 1


if __name__ == '__main__':
    get_links('https://opendatasus.saude.gov.br')
