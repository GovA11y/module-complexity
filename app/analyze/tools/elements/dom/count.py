# app/analyze/tools/elements/dom/count.py
from bs4 import BeautifulSoup
from pyroscope import tag_wrapper


@tag_wrapper({ 'state.function': 'count_dom_elements' })
def count_dom_elements(html):
    '''Counts all the DOM elements in a given HTML.'''

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html, 'html.parser')

    # Use the find_all method, which returns a list of all tags found
    # Count the length of this list to get the total number of DOM elements
    dom_elements = soup.find_all(True)

    # Return the count of all DOM elements
    return len(dom_elements)
