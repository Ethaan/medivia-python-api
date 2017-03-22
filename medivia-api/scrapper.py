import requests
from bs4 import BeautifulSoup


def get_page_content(url, reader):
    page = requests.get(url)
    parser = BeautifulSoup(page.content, 'html.parser')
    return reader(parser)
