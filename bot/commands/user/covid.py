from plugins import covid19_script
from functions import general
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def message_builder():
    c = covid19_script.Covid()

    if c.incremento_p_contagiati>=0:
        p_cont = "+"+str(c.incremento_p_contagiati)
    else:
        p_cont = c.incremento_p_contagiati
    
    if c.incremento_p_guariti>=0:
        p_guar = "+"+str(c.incremento_p_guariti)
    else:
        p_guar = c.incremento_p_guariti
    
    if c.incremento_p_deceduti>=0:
        p_dec = "+"+str(c.incremento_p_deceduti)
    else:
        p_dec = c.incremento_p_deceduti
    
    if c.incremento_p_tamponi>=0:
        p_tamp = "+"+str(c.incremento_p_tamponi)
    else:
        p_tamp = c.incremento_p_tamponi

    

    txt = str(general.txtReader('daily_report')).format(c.nuovi_positivi,p_cont, c.nuovi_guariti,p_guar, c.nuovi_deceduti, p_dec, c.nuovi_tamponi, p_tamp,c.terapia_intensiva,c.rapp_tamponi_positivi, c.totale_positivi, c.dimessi_guariti, c.deceduti, (c.deceduti + c.dimessi_guariti + c.totale_positivi), c.tamponi)

    #message = '🦠 <b>[DAILY REPORT | COVID-19]</b> 🦠\n\nCountry: <b>{}</b> 🇮🇹\n\n⛑ Confirmed: <b>{}</b>\n⛑ New Cases: <b>{}</b>\n⚠️ Critical: <b>{}</b>\n\n✅ Recovered: <b>{}</b>\n\n☠️ Deaths: <b>{}</b>\n☠️ New deaths: <b>{}</b>\n'.format(country, confirmed, new_cases, critical, recovered, deaths, new_deaths)
    
    return txt

def init(update, context):
    keyboard = [[InlineKeyboardButton('Sorgente dati 📊', url = 'https://github.com/pcm-dpc/COVID-19')],[InlineKeyboardButton('Info 🦠', url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?area=nuovoCoronavirus&id=5351&lingua=italiano&menu=vuoto')]]
    chat = update.message.chat_id
    user = update.message.from_user.id
    if chat == user:
        update.message.reply_text(message_builder(), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='HTML')
    else:
        update.message.reply_text('Comando solo per chat private')
