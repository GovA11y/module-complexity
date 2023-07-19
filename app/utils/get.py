# app/utils/get.py
import requests
from bs4 import BeautifulSoup
from pyroscope import tag_wrapper


def get_html(url):
    '''Fetches a webpage and returns its HTML.'''
    response = requests.get(url)
    return response.text