import os
import sqlite3

# Ta bort gammal databas för att börja från början
if os.path.exists("mynewapp.db"):
    os.remove("mynewapp.db")

# Importera funktioner från app.py
from app import connect, init_db, anonymize_data, clear_test_data

print("=" * 40)
print("TESTER FÖR APP.PY")
print("=" * 40)

# TEST 1: GDPR-TEST
print("\n🔒 GDPR-TEST: Anonymisera data")
print("-" * 30)

# Skapa databas med testdata
init_db()

# Kör anonymisering
anonymize_data()

# Kontrollera resultatet
conn = connect()
cursor = conn.cursor()
cursor.execute("SELECT name FROM personer WHERE id=1")
resultat = cursor.fetchone()

if resultat and resultat[0] == "Anonymiserad Namn":
    print("✅ PASS: Data anonymiserades korrekt för GDPR")
else:
    print("❌ FAIL: Data anonymiserades INTE korrekt")

conn.close()

# TEST 2: UNIT TEST - Databas skapas
print("\n🧪 UNIT TEST: Databas funktioner")
print("-" * 30)

# Rensa och testa från början
if os.path.exists("mynewapp.db"):
    os.remove("mynewapp.db")

# Testa att databasen skapas
init_db()

# Kontrollera att databasfilen finns
if os.path.exists("mynewapp.db"):
    print("✅ PASS: Databasfil skapades")
else:
    print("❌ FAIL: Databasfil skapades INTE")

# Kontrollera att tabellen finns
conn = connect()
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='personer'")
tabell = cursor.fetchone()

if tabell:
    print("✅ PASS: Tabellen 'personer' skapades")
else:
    print("❌ FAIL: Tabellen skapades INTE")

# Kontrollera att data lades till
cursor.execute("SELECT COUNT(*) FROM personer")
antal = cursor.fetchone()[0]

if antal == 2:
    print("✅ PASS: 2 personer lades till i tabellen")
else:
    print(f"❌ FAIL: Fel antal personer ({antal} istället för 2)")

conn.close()

print("\n" + "=" * 40)
print("TESTER KLARA")
print("=" * 40)