# app/main.py
from analyze import get_variables


url = 'https://bentleyhensel.com'


variables = get_variables(url)

print('\nVariables:\n\n', variables, '\n')