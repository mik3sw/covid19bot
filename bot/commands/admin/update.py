from utils import decorator
from functions import database, general

@decorator.ownerbot
def init(update, context):
    d = database.DB()
    for x in d.db_read():
        try:
            context.bot.send_message(chat_id = x, text=general.txtReader('aggiornamento'), parse_mode= 'HTML')
        except:
            print('chat: {} not found'.format(x))