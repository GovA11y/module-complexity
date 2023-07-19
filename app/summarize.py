from bs4 import BeautifulSoup
import requests






def calculate_complexity(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Number of Interactive Elements
    interactive_elements = ['a', 'button', 'input', 'select', 'textarea']
    interactive_count = sum(len(soup.find_all(tag)) for tag in interactive_elements)

    # Number of DOM Elements
    dom_count = len(soup.find_all(True))

    # Number of Media Elements
    media_elements = ['img', 'audio', 'video', 'picture', 'track', 'source']
    media_count = sum(len(soup.find_all(tag)) for tag in media_elements)

    # Number of iFrames
    iframe_count = len(soup.find_all('iframe'))

    # Number of Tables
    table_count = len(soup.find_all('table'))

    # Compile the results
    result = {
        'interactive_count': interactive_count,
        'dom_count': dom_count,
        'media_count': media_count,
        'iframe_count': iframe_count,
        'table_count': table_count,
    }

    return result

url = "https://www.example.com"
print(calculate_complexity(url))
