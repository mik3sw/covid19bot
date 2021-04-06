from plugins import covid19_script
import time
import datetime
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import decorator
from functions import database, general


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


def alarm(context):
    d = database.DB()
    keyboard = [[InlineKeyboardButton('Sorgente dati 📊', url = 'https://github.com/pcm-dpc/COVID-19')],[InlineKeyboardButton('Info 🦠', url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?area=nuovoCoronavirus&id=5351&lingua=italiano&menu=vuoto')]]
    for x in d.db_read():
        try:
            context.bot.send_message(chat_id = x, text=message_builder(), reply_markup = InlineKeyboardMarkup(keyboard), parse_mode= 'HTML')
        except:
            print('chat: {} not found'.format(x))

@decorator.ownerbot
def set_timer(update, context):
    #chat_id = update.message.chat_id
    h = 19
    m = 00

    if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
    t = datetime.time(h-2, m, 00)
    new_job = context.job_queue.run_daily(alarm, t, days=(0, 1, 2, 3, 4, 5, 6), context=None, name='covidreport')
    context.chat_data['job'] = new_job
    update.message.reply_text('Covid-19 report setted [DAILY][{}:{}]'.format(h, m))

def unset(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('Nothing to do here')
        return

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Covid-19 report unsetted')