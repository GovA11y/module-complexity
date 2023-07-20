# app/analyze/tools/elements/__init__.py
from .dom.count import count_dom_elements
from .dom.depth import calculate_dom_depth
from bs4 import BeautifulSoup
import requests
import cssutils
import logging


cssutils.log.setLog(logging.getLogger('cssutils'))
cssutils.log.setLevel(logging.FATAL)


def get_dom_vars(html):
    dom_count = count_dom_elements(html)
    dom_depth = calculate_dom_depth(html)

    # Generate Response
    response = {
        'dom_count': dom_count,
        'dom_depth': dom_depth
    }
    return response


def get_css_vars(html, url, css_files):
    try:
        total_css_size_kb = 0
        count_css_rules = 0
        count_css_selectors = 0

        for css_content in css_files:
            total_css_size_kb += len(css_content.encode('utf-8')) / 1024  # Get size of content in bytes, convert to kilobytes

            # Parse the CSS content
            sheet = cssutils.parseString(css_content)

            # Count the number of CSS rules
            count_css_rules += sheet.cssRules.length

            # Count the number of CSS selectors
            for rule in sheet:
                if rule.type == rule.STYLE_RULE:  # Only style rules have selectors
                    count_css_selectors += len(rule.selectorList)

        soup = BeautifulSoup(html, 'html.parser')
        count_inline_css = len(soup.select('[style]'))

        # Generate Response
        response = {
            'count_external_css': len(css_files),
            'total_css_size_kb': total_css_size_kb,
            'count_inline_css': count_inline_css,
            'count_css_rules': count_css_rules,
            'count_css_selectors': count_css_selectors,
        }
        return response
    except Exception as e:
        print("Caught exception in get_css_vars: ", str(e))
        return None