import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import urllib.request, urllib.error, urllib.parse

import validators

num_niveis = 2

headers = {'Content-Type': 'text/html', 'User-Agent': 'Mozilla/5.0'}

def download_webpage(url, num):

    req = Request(
        url=url, 
        headers=headers
    )
    response = urlopen(req)

    #response = urllib.request.urlopen(url)
    webContent = response.read().decode(response.headers.get_content_charset())#.decode('UTF-8')

    f = open(str(num)+'.txt', 'w', encoding='UTF-8')
    f.write(webContent)
    f.close

def get_links(url):

    num = 0

    links = []
    website = requests.get(url, headers=headers)
    website_text = website.text

    soup = BeautifulSoup(website_text, 'html.parser')

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    for link in links:

        if(str(link) != 'None'):
            if validators.url(link):
                download_webpage(link, num)
                num += 1

get_links('https://opendatasus.saude.gov.br')