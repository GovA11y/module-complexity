# CSS Elements

Number of CSS files: Total count of externally linked CSS files.

Size of CSS files: Total size in kilobytes of all CSS files combined.

Count of inline CSS: Total count of CSS defined within style tags in the HTML document.

Count of external CSS: Total count of CSS defined in externally linked CSS files.

Count of CSS rules: Total count of rules found in the CSS. A rule is a block including a selector and declaration block, e.g., p { color: red; }.

Count of CSS selectors: Total count of selectors found in the CSS code. A selector is the part of a CSS rule set that actually selects the content you want to style.

Specificity of selectors: The measure of the specificity of each selector used in the CSS. Specificity is a weight that is applied to a given CSS declaration, determined by the number of each selector type in the matching selector.

Use of !important: The total count of !important declarations in the CSS code. This could be an indicator of complexity as !important increases the weight of a CSS rule and can lead to maintenance issues and specificity war.

Specificity complexity: This could be a weighted average of the specificity of all selectors, or another statistic that gives an idea of the overall specificity of the CSS. High specificity complexity might indicate that the webpage's styles are tightly coupled with the HTML and hard to maintain.

# Fetch html and css files from the site

html = get_html('https://example.com')
css_files = get_external_css(html, 'https://example.com')

# 1. Number of css files

number_of_css_files = len(css_files)

# Later we will populate these variables

# 2. Size of css files

total_css_size_kb = None

# 3. Count of inline css

count_inline_css = None

# 4. Count of external css

count_external_css = None

# We'll use CSS parser to fetch these metrics

# 5. Count of css rules

count_css_rules = None

# 6. Count of css selectors

count_css_selectors = None

# 7. Specificity of selectors

specificity_of_selectors = None

# 8. Use of !important

count_important = None

# 9. Specificity complexity

specificity_complexity = None
