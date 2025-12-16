## Mynewapp 
- Smidig och lätt system för säkerställa att testdata är nogranat i integrationen med GDPR

## Docker 
- Appen är i isolerade Docker container med hjälp av Python 3 (VS)



### Förutsättningar
- Docker och Docker Compose
- Python 3.9+
- Git


### Kör med Docker
- I terminal ska projektmappen nås (TestD2) och sen körs följande kommando för att bygga upp container 


´´´docker-compose up --build´´´


docker --version
docker build -t my-python-app .
docker images
docker run my-python-app
docker run -it my-python-app
docker run --rm my-python-app



Pusha ändringar när du redan har remote:
bash
# 1. Se vad som ändrats
git status

# 2. Lägg till specifika filer eller alla
git add app.py test_enkel.py Dockerfile
# ELLER
git add .

# 3. Skapa commit
git commit -m "Fixade bugg i anonymiseringsfunktionen"

# 4. Push till GitHub
git push



markdown
# 📊 GDPR-compliant Person Data Manager

En Python-applikation för att hantera personuppgifter på ett GDPR-säkert sätt med anonymisering och automatiserade tester.

## 🚀 Funktioner

- **Databashantering** - SQLite-databas för personuppgifter
- **GDPR-anonymisering** - Automatisk anonymisering av personuppgifter
- **Enhetstester** - Automatiserade tester för kodkvalitet
- **CI/CD Pipeline** - GitHub Actions för automatisk testning
- **Docker support** - Kör i container för enkel distribution

## 📁 Projektstruktur
TestD2/
├── app.py # Huvudapplikation
├── test_enkel.py # GDPR- och enhetstester
├── Dockerfile # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── .github/workflows/ # GitHub Actions workflows
│ └── build-test.yml # CI/CD pipeline
├── .gitignore # Ignorerade filer
└── README.md # Denna fil

text

## ⚡ Snabbstart

### Lokal körning
```bash
# Installera Python 3.9 eller senare
python --version

# Kör huvudapplikationen
python app.py

# Kör testerna
python test_enkel.py
Med Docker
bash
# Bygg Docker image
docker build -t gdpr-app .

# Kör applikationen
docker run --rm gdpr-app

# Kör testerna
docker run --rm gdpr-app python test_enkel.py
Med Docker Compose
bash
docker-compose up
🧪 Tester
Projektet innehåller två typer av automatiserade tester:

1. GDPR-test
Kontrollerar att personuppgifter anonymiseras korrekt

Säkerställer GDPR-efterlevnad

2. Enhetstester
Testar databasanslutning och tabellskapande

Verifierar att grunddata läggs till korrekt

Kör alla tester:

bash
python test_enkel.py
🔒 GDPR-kompatibilitet
Applikationen följer GDPR-principer genom:

Anonymisering - Alla namn ersätts med "Anonymiserad Namn"

Datarensning - Funktion för att rensa all data

Säker hantering - Inga känsliga uppgifter i versionkontroll

🛠️ Teknologier
Python 3.9 - Backend-språk

SQLite3 - Databashantering

Docker - Containerisering

GitHub Actions - CI/CD

unittest - Testramverk

📊 Databasstruktur
sql
CREATE TABLE personer (
    id INTEGER PRIMARY KEY,
    name TEXT,
    ålder INTEGER
);
🤖 GitHub Actions
Vid varje push/pull request till main-branchen körs automatiskt:

Bygg- och testprocess

GDPR-tester

Enhetstester

Status badge: https://github.com/Ali1586/TestD2/actions/workflows/build-test.yml/badge.svg

📝 Exempelkörning
text
Starta testa data

[Steg 1: Initiera & Visa Basdata]
ID: 1, Namn: Sara, Ålder: 25
ID: 2, Namn: Matteo, Ålder: 30

[Steg 2: Anonymisera alla rader]
ID: 1, Namn: Anonymiserad Namn, Ålder: 25
ID: 2, Namn: Anonymiserad Namn, Ålder: 30

[Steg 3: Rensa all data]
testdata är klart
🚨 Säkerhet
Databasfiler (.db) är undantagna från versionkontroll via .gitignore

Inga känsliga uppgifter committas till git

Anonymisering är standard för GDPR-efterlevnad

🆘 Felsökning
Vanliga problem:
"Database is locked" - Stäng andra instanser av appen

ImportError - Se till att du har Python 3.9+

Docker build misslyckas - Kontrollera att Docker Desktop är igång

Lösningar:
bash
# Rensa databascache
rm mynewapp.db

# Reinstallera beroenden (om Docker)
docker system prune -a
docker build -t gdpr-app .
👥 Bidra
Forka repot

Skapa en feature branch

Commit dina ändringar

Pusha till branchen

Skapa en Pull Request