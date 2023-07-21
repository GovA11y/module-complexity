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


def specificity(selector):
        # Calculate specificity based on W3C rules. This won't be as accurate as it parses with regex.
        import re

        # Don't include universal selector
        selector = re.sub(r'\*', '', selector)

        #ID selectors
        a = len(re.findall(r'\#[\w\-]+', selector))

        # Class selectors, attributes selectors, or pseudo-classes
        b = len(re.findall(r'(\.[\w\-]+)|(\[[\w\s\-]+])|(:[\w\-]+)', selector))

        # Element Selectors or pseudo-elements
        c = len(re.findall(r'((^|[\s\+\>]+)[\w\-]+)|(::[\w\-]+)', selector))

        return a*100 + b*10 + c


def get_css_vars(html, url, css_files):
    try:
        if css_files is None:
            raise TypeError("css_files can't be None")
        total_css_size_kb = 0
        count_css_rules = 0
        count_css_selectors = 0
        count_important = 0
        total_specificity_points = 0

        for css_content in css_files:
            total_css_size_kb += len(css_content.encode('utf-8')) / 1024

            sheet = cssutils.parseString(css_content)

            count_css_rules += sheet.cssRules.length

            for rule in sheet:
                if rule.type == rule.STYLE_RULE:  # Only style rules have selectors
                    selectors = rule.selectorList
                    count_css_selectors += len(selectors)

                    for selector in selectors:
                        total_specificity_points += specificity(selector.selectorText)

                    for property in rule.style:
                        if property.priority == 'important':
                            count_important += 1

        soup = BeautifulSoup(html, 'html.parser')
        count_inline_css = len(soup.select('[style]'))

        # Average specificity per selector
        specificity_of_selectors = total_specificity_points / count_css_selectors if count_css_selectors else 0

        # Determine complexity
        if specificity_of_selectors < 10:
            specificity_complexity = 'low'
        elif specificity_of_selectors < 30:
            specificity_complexity = 'medium'
        else:
            specificity_complexity = 'high'

        response = {
            'count_external_css': len(css_files),
            'total_css_size_kb': total_css_size_kb,
            'count_inline_css': count_inline_css,
            'count_css_rules': count_css_rules,
            'count_css_selectors': count_css_selectors,
            'specificity_of_selectors': specificity_of_selectors,
            'count_important': count_important,
            'specificity_complexity': specificity_complexity,
        }
        return response
    except AttributeError as e:
        print("Caught AttributeError in get_css_vars: ", str(e))
        return None
    except TypeError as e:
        print("Caught TypeError in get_css_vars: ", str(e))
        return None
    except Exception as e:  # Generic Exception should be last
        print("Caught an unexpected exception in get_css_vars: ", str(e))
        return None