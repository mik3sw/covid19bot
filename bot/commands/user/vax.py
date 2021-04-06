from plugins import vaccines_script
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from functions import general

def message_builder():
    v = vaccines_script.Vaccines()
    totale = v.get_data_tot()
    giorni_necessari, new_date = v.calcolo_pazzerello()
    txt = str(general.txtReader('vax_report')).format(totale["totale_somministrazioni"],
                                                      v.get_percentuale_somministrazioni(),
                                                      totale["totale_consegnate"],
                                                      v.get_media_giornaliera(),
                                                      v.get_percentuale_popolazione(),
                                                      giorni_necessari,
                                                      new_date)
    return txt

def init(update, context):
    keyboard = [[InlineKeyboardButton('Sorgente dati 📊', url = 'https://github.com/italia/covid19-opendata-vaccini')],[InlineKeyboardButton('Info 🧪', url = 'https://www.governo.it/it/cscovid19/report-vaccini/')]]
    chat = update.message.chat_id
    user = update.message.from_user.id
    if chat == user:
        update.message.reply_text(message_builder(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
    else:
        update.message.reply_text('Comando solo per chat private')
