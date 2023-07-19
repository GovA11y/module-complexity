# app/main.py
from analyze import get_variables
import os
from dotenv import load_dotenv


load_dotenv()
url = 'https://bentleyhensel.com'


variables = get_variables(url)

print('\nVariables:\n\n', variables, '\n')