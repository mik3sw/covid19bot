from plugins import covid19_script
from functions import general
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def message_builder():
    try:
        c = covid19_script.Covid()
        c1, c2, c3, c4 = c.get_media_settimanale()
        txt= txt = str(general.txtReader('weekly_report')).format(c1, c2, c3, c4)
    except:
        txt = 'error'

    
    return txt

def init(update, context):
    keyboard = [[InlineKeyboardButton('Sorgente dati 📊', url = 'https://github.com/pcm-dpc/COVID-19')],[InlineKeyboardButton('Info 🦠', url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?area=nuovoCoronavirus&id=5351&lingua=italiano&menu=vuoto')]]
    chat = update.message.chat_id
    user = update.message.from_user.id
    if chat == user:
        update.message.reply_text(message_builder(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
    else:
        update.message.reply_text('Comando solo per chat private')