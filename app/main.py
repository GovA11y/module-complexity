# app/main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyze import get_variables

url = 'https://www.digital.gov'

variables = get_variables(url)

print('\nVariables:\n\n', variables, '\n')
