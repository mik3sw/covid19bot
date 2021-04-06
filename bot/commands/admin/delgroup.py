from utils import decorator
from functions import database, general

@decorator.general_admin
def init(update, context):
    d = database.DB()
    chat = update.message.chat_id
    status, mess = d.db_remove(chat)
    if status:
        update.message.reply_text(general.txtReader('db_remove_true'), parse_mode='HTML')
    else:
        update.message.reply_text(general.txtReader('db_remove_false')+'\n[LOG]: {}'.format(mess), parse_mode='HTML')

    