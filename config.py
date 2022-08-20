import os
from dotenv import load_dotenv


load_dotenv()


GOOGLE_SECRET_KEY = os.getenv('GOOGLE_SECRET_KEY')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
