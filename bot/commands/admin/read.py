from utils import decorator
from functions import database, general

@decorator.ownerbot
def init(update, context):
    d = database.DB()
    lista = d.db_read()
    #message = ''
    users = 0
    for x in lista:
        users = users + 1
        #message = message + str(x) + '\n'
    message = "Utenti iscritti: <b>{}</b>".format(users)
    update.message.reply_text(message, parse_mode='HTML')