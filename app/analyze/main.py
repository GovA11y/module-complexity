# app/analyze/main.py
"""
app/analyze/main.py

Purpose of this script and scripts in the analyze directory is to return the metrics which are used to calculate page complexity.

"""
from .tools.elements import get_dom_vars, get_css_vars
from app.utils import get_html, get_external_css, get_external_js


def get_variables(url):
    html = get_html(url)
    css_files = get_external_css(html, url)
    # Dom Vars
    dom_vars = get_dom_vars(html)
    print('dom_vars:', dom_vars)

    # CSS Vars
    css_vars = get_css_vars(html, url, css_files)
    print('css_vars:', css_vars)

    all_vars = {}
    if dom_vars is not None:
        all_vars.update(dom_vars)

    if css_vars is not None:
        all_vars.update(css_vars)

    return all_vars