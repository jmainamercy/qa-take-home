"""Configuration comes from environment variables, with defaults for the public practice API.
Nothing is hard-coded inside the tests."""
import os

BASE_URL = os.getenv("BOOKER_BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("BOOKER_USERNAME", "admin")          
PASSWORD = os.getenv("BOOKER_PASSWORD", "password123")  
MAX_RESPONSE_SECONDS = float(os.getenv("BOOKER_MAX_SECONDS", "2"))
