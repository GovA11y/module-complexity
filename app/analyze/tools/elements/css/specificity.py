# app/analyze/tools/elements/css/specificity.py
import re

def specificity(selector):
    # Calculate specificity based on W3C rules. This won't be as accurate as it parses with regex.

    # Don't include universal selector
    selector = re.sub(r'\*', '', selector)

    #ID selectors
    a = len(re.findall(r'\#[\w\-]+', selector))

    # Class selectors, attributes selectors, or pseudo-classes
    b = len(re.findall(r'(\.[\w\-]+)|(\[[\w\s\-]+])|(:[\w\-]+)', selector))

    # Element Selectors or pseudo-elements
    c = len(re.findall(r'((^|[\s\+\>]+)[\w\-]+)|(::[\w\-]+)', selector))

    return a*100 + b*10 + c
