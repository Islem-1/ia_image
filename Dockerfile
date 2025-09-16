# Image de base officielle Python
FROM python:3.13-slim

# Définir le dossier de travail
WORKDIR /app

# Copier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Variables d’environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Commande de démarrage
CMD ["flask", "run"]
