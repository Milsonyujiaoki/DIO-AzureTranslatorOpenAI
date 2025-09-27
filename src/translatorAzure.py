import requests
from bs4 import BeautifulSoup

def translate_text(text, target_language):
    subscription_key = ""
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
    body = [{
        "text": text
    }]
    response = requests.post(f"{endpoint}&to={target_language}", headers=headers, json=body)
    if response.status_code == 200:
        translation = response.json()[0]["translations"][0]["text"]
        return translation
    else:
        print(f"Error: {response.status_code}")
        return None