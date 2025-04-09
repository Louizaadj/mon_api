import requests
import os
from dotenv import load_dotenv

def fetch_apod():
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")  
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("🌌 Image du jour :", data.get('title'))
        print("📅 Date :", data.get('date'))
        print("🧠 Explication :", data.get('explanation'))
        print("🔗 Image HD :", data.get('hdurl'))
    else:
        print("❌ Erreur :", response.status_code, response.text)

if __name__ == "__main__":
    fetch_apod()
