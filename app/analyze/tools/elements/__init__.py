# app/analyze/tools/elements/__init__.py
from .dom.count import count_dom_elements
from .dom.depth import calculate_dom_depth

def get_dom_vars(html):
    dom_count = count_dom_elements(html)
    dom_depth = calculate_dom_depth(html)

    # Generate Response
    response = {
        'dom_count': dom_count,
        'dom_depth': dom_depth
    }
    return response