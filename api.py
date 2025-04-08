from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/apod", methods=["GET"])
def get_apod():
    api_key = os.getenv("NASA_API_KEY")
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "title": data.get("title"),
            "date": data.get("date"),
            "explanation": data.get("explanation"),
            "hdurl": data.get("hdurl")
        })
    else:
        return jsonify({"error": "API NASA a échoué"}), response.status_code
    
@app.route("/")
def home():
    return "Bienvenue sur l'API NASA de Louiza 🚀 !Va sur /apod pour découvrir la photo du jour."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
