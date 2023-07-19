# app/analyze/tools/elements/dom/depth.py
from bs4 import BeautifulSoup
from pyroscope import tag_wrapper
import requests
from app.utils import get_html

@tag_wrapper({'state.function': 'calculate_dom_depth'})
def calculate_dom_depth(html):
    soup = BeautifulSoup(html, 'html.parser')
    return get_max_depth(soup.html, 0)  # Begin parsing from the <html> tag

def get_max_depth(bs4_element, current_depth):
    # Base case: if bs4_element has no child tags, return current_depth
    if len(bs4_element.find_all(recursive=False)) == 0:
        return current_depth
    # Recursive case: return the maximum max_depth of all child tags, plus 1
    else:
        return max([get_max_depth(child, current_depth + 1) for child in bs4_element.find_all(recursive=False)])
