# app/analyze/tools/elements/__init__.py
from .dom.count import count_dom_elements, get_html

def get_dom_vars(url):
    html = get_html(url)
    dom_count = count_dom_elements(html)
    response = {
        'dom_count': dom_count
    }
    return response