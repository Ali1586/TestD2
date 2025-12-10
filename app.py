import sqlite3
import os

db_namn = "mynewapp.db"

def connect():
    return sqlite3.connect(db_namn)

def init_db():

    conn=connect()
    cursor=conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS personer (
       id INTEGER PRIMARY KEY,
       name TEXT,
       ålder INTEGER
     )
''')


    cursor.execute('SELECT * FROM personer')
    resultat = cursor.fetchall()
    if resultat:
        conn.close()
        return

    cursor.executemany('''
        INSERT INTO personer(id, name, ålder)
        VALUES(?,?,?)                              
    ''', [(1, 'Sara', 25),
        (2, 'Matteo', 30)])
 
    conn.commit()
    conn.close()

    


def add_new_person_data():  
    
    conn=connect()
    cursor=conn.cursor()

    cursor.execute('SELECT * FROM personer')
    resultat = cursor.fetchall()

    for rad in resultat:
        print(f"ID: {rad[0]}, Namn: {rad[1]}, Ålder: {rad[2]}")
    
    conn.close()
      
def clear_test_data():  
    
    conn=connect()
    cursor=conn.cursor()

    cursor.execute('DELETE FROM personer')

    conn.commit()
    conn.close()


def anonymize_data():  
    conn = connect()
    
    cursor=conn.cursor()

    cursor.execute('''
        UPDATE personer
        SET name = 'Anonymiserad Namn'
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":

    
    print('Starta testa data')
    
    print("\n[Steg 1: Initiera & Visa Basdata]")
    init_db()
    add_new_person_data()


    print("\n[Steg 2: Anonymisera alla rader]")
    anonymize_data()
    add_new_person_data()
    
    print("\n[Steg 3: Rensa all data]")
    clear_test_data()

    add_new_person_data()

    print('testdata är klart')

    


    

