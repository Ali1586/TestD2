import sqlite3
import os

def init_db():
    if os.path.exists('mynewapp.db'):
        os.remove('mynewapp.db')
    conn=sqlite3.connect('mynewapp.db')

    cursor=conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS personer (
       id INTIGER PRIMERY KEY,
       name TEXT,
       ålder INTEGER
)
''')

    cursor.execute('''
    INSERT INTO personer(id,name,ålder)
    VALUES(?,?,?)                              
''',(1,'Sara',25))
 
    conn.commit()

    cursor.execute('SELECT * FROM personer')
    resultat = cursor.fetchall()

    for rad in resultat:
        print(f"ID: {rad[0]}, Namn: {rad[1]}, Ålder: {rad[2]}")

    conn.close()

if __name__ == "__name__":
    #init_database()
    #display_users()
    
    
    init_db()

    #print("\nContainer is running. Press Ctrl+C to exit.")

    #try:
     #   while True:  # Denna loop håller containern igång
      #      pass
    #except KeyboardInterrupt:
        #print("\nShutting down...")
