from functions import database, general

def init(update, context):
    d = database.DB()
    chat = update.message.chat_id
    user = update.message.from_user.id
    if chat == user:
        status, mess = d.db_insert(chat)
        if status:
            update.message.reply_text(general.txtReader('db_insert_true'), parse_mode='HTML')
        else:
            update.message.reply_text(general.txtReader('db_insert_false')+'\n[LOG]: {}'.format(mess), parse_mode='HTML')
    else:
        update.message.reply_text('Comando solo per chat private')

    