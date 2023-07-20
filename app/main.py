# app/main.py
from analyze import get_variables


url = 'https://www.digital.gov'


variables = get_variables(url)

print('\nVariables:\n\n', variables, '\n')