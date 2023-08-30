# app/analyze/tools/elements/javascript/main.py
"""
This is where we get all of the javascript variables. In other modules, we will `from javascript import get_js_vars`
when those other modules run js_vars = get_js_vars(...???...) they will be returned values in the same format as below

{'count_external_css': 1, 'total_css_size_kb': 307.4462890625, 'count_inline_css': 1, 'count_css_rules': 1795, 'count_css_selectors': 2977, 'specificity_of_selectors': 23.5226738327175, 'count_important': 16, 'specificity_complexity': 'medium'}
"""
