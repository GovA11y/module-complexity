# app/utils/get.py
import requests
from bs4 import BeautifulSoup
from pyroscope import tag_wrapper


@tag_wrapper({ 'state.function': 'get_html' })
def get_html(url):
    '''Fetches a webpage and returns its HTML.'''
    response = requests.get(url)
    return response.text


@tag_wrapper({ 'state.function': 'get_external_css' })
def get_external_css(html, url):
    '''Fetches all externally linked CSS files in a given HTML.'''
    soup = BeautifulSoup(html, 'html.parser')
    css = []

    for link in soup.find_all("link"):
        if "stylesheet" in link.get("rel", []):            # If link is a stylesheet
            css_url = link.get("href")                     # Get URL of CSS file
            if css_url and not css_url.startswith("http"): # If URL is relative, turn it into an absolute URL
                css_url = url.rstrip("/") + "/" + css_url.lstrip("/")
            try:
                css_response = requests.get(css_url)
                if css_response.status_code == 200:        # Ensure the request was successful
                    css.append(css_response.text)          # Store the fetched CSS code
            except:
                pass                                       # If fetch fails, skip this file

    return css


@tag_wrapper({ 'state.function': 'get_external_js' })
def get_external_js(html, url):
    '''Fetches all externally linked JS files in a given HTML.'''
    soup = BeautifulSoup(html, 'html.parser')
    js = []

    for script in soup.find_all("script"):
        script_url = script.get("src")                    # Get URL of Javascript file
        if script_url and not script_url.startswith("http"): # If script tag has a src attribute and URL is relative, turn it into an absolute URL
            script_url = url.rstrip("/") + "/" + script_url.lstrip("/")
        try:
            js_response = requests.get(script_url)
            if js_response.status_code == 200:            # Ensure the request was successful
                js.append(js_response.text)               # Store the fetched Javascript code
        except:
            pass                                          # If fetch fails, skip this file
    return js