from dotenv import load_dotenv
import os

def getKey():
    load_dotenv()
    secret_key = os.getenv('API_KEY')
    return secret_key