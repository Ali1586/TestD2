# Använd Python som basbild
FROM python:3.9-slim

# Ställ in arbetskatalog
WORKDIR /app

# Kopiera koden
COPY app.py .
COPY test_enkel.py .

# Kör appen när containern startar
CMD ["python", "app.py"]