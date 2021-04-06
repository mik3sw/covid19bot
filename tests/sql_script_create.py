import sqlite3

conn = sqlite3.connect('Groups.db')  
c = conn.cursor()
c.execute('CREATE TABLE gruppo(id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER NOT NULL UNIQUE);')                
conn.commit()
conn.close()