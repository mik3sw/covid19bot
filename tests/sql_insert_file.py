import sqlite3
from sqlite3 import Error


try:
    sqliteConnection = sqlite3.connect('Groups.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    chat = [12131231231, 1245546, 23212313, 463452413, 235234234]

    for x in chat:
        sqlite_insert_query = "INSERT INTO gruppo (chat_id) VALUES ({})".format(x)
        print(x)
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()

    
    print("Record inserted successfully into COVIDBOT table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")