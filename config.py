import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


