import requests
import json
from secretRetriever import getKey

def getJSON(url,apiHost):
    apiKey = getKey()
    # Set the headers
    headers = {
    "X-Rapidapi-Key": apiKey,
    "X-Rapidapi-Host": apiHost
    }
    response = requests.get(url,headers=headers)
    return response.json()

