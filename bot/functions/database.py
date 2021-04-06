import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self):
        self.database_file = 'Groups.db'
    
    def db_insert(self, chat_id):
        ris = False
        lista = self.db_read()
        can_insert = True
        if chat_id in lista:
            can_insert = False
            #print('utente già presente in lista')
        if can_insert == True:
            try:
                sqliteConnection = sqlite3.connect(self.database_file)
                cursor = sqliteConnection.cursor()
                #print("Successfully Connected to SQLite")
                sqlite_insert_query = "INSERT INTO gruppo (chat_id) VALUES ({})".format(chat_id)
                cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                #print("New chat_id [{}] inserted successfully ".format(chat_id))
                cursor.close()
                mess = 'No errors'
                ris = True

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)

            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    #clprint("The SQLite connection is closed")
            return ris, mess
        else:
            mess = 'Utente/Gruppo già presente in lista'
            return False, mess
    
    def db_read(self):
        conn = sqlite3.connect(self.database_file)
        c = conn.cursor()
        c.execute('SELECT chat_id FROM gruppo')
        data = c.fetchall()
        c.close()
        x = self.create_list(data)
        return x
    
    def create_list(self, data):
        lista = []
        for item in data:
            lista.append(item[0])
        return lista
    
    def db_remove(self, chat_id):
        lista = self.db_read()
        can_delete = False
        if chat_id in lista:
            can_delete = True
        if can_delete == True:
            try:
                conn = sqlite3.connect(self.database_file)
                c = conn.cursor()
                c.execute('DELETE FROM gruppo WHERE chat_id = {};'.format(chat_id))
                conn.commit()
                c.close()
                mess = 'no errors'
                return True, mess
            except:
                mess = 'Errore database'
                return False, mess
        else:
            mess = 'Utente/Gruppo non in lista'
            return False, mess



    

