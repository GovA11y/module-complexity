# app/analyze/main.py
"""
app/analyze/main.py

Purpose of this script and scripts in the analyze directory is to return the metrics which are used to calculate page complexity.

"""
from .tools.elements import get_dom_vars
from app.utils import get_html


def get_variables(url):
    html = get_html(url)
    dom_vars = get_dom_vars(html)

    all_vars = {
        **dom_vars
    }
    return all_vars