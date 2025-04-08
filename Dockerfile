# Prend une image légère de Python
FROM python:3.10-slim

# Crée un dossier de travail dans la boîte
WORKDIR /app

# Copie le script dans la boîte
COPY main.py .

# Installe la librairie "requests"
RUN pip install requests

# Démarre le script quand on lance la boîte
CMD ["python", "main.py"]
