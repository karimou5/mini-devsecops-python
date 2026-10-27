# Démo : image volontairement mal configurée (tourne en root, pas d'instruction USER)
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
