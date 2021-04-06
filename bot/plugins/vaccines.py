from plugins import vaccines_script
import time
import datetime
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import decorator
from functions import database, general


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


def alarm(context):
    d = database.DB()
    keyboard = [[InlineKeyboardButton('Sorgente dati 📊', url = 'https://github.com/italia/covid19-opendata-vaccini')],[InlineKeyboardButton('Info 🧪', url = 'https://www.governo.it/it/cscovid19/report-vaccini/')]]
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

    if 'job1' in context.chat_data:
            old_job = context.chat_data['job1']
            old_job.schedule_removal()
    t = datetime.time(h-2, m, 00)
    new_job = context.job_queue.run_daily(alarm, t, days=(0, 1, 2, 3, 4, 5, 6), context=None, name='vaccinesreport')
    context.chat_data['job1'] = new_job
    update.message.reply_text('Vaccines report setted [DAILY][{}:{}]'.format(h, m))

def unset(update, context):
    if 'job1' not in context.chat_data:
        update.message.reply_text('Nothing to do here')
        return

    job = context.chat_data['job1']
    job.schedule_removal()
    del context.chat_data['job1']

    update.message.reply_text('Vaccines report unsetted')