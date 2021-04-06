import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('Groups.db')
c = conn.cursor()

def create_list(data):
        lista = []
        for item in data:
            lista.append(item[0])
        return lista

def read_from_db():
    c.execute('SELECT chat_id FROM gruppo')
    data = c.fetchall()
    x = create_list(data)
    return x


for x in read_from_db():
    print(x)


    


