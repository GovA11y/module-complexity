# app/__init__.py
import os
from dotenv import load_dotenv
import pyroscope


load_dotenv()


# Configure Pyroscope
pyroscope.configure(
    application_name=os.getenv("PYROSCOPE_APPLICATION_NAME"),
    server_address=os.getenv("PYROSCOPE_SERVER"),
)

