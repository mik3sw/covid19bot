# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import config, dialogs, commands, errors, plugins, functions
import os
import sys
from threading import Thread
from utils import decorator


def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher

    # restart function 
    # ===============================================
    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    #only the owner of the bot can use restart command
    @decorator.ownerbot  
    def restart(update, context):
        update.message.reply_text('<b>[SYSTEM]</b>\n\nThe bot is now restarting...', parse_mode='HTML')
        Thread(target=stop_and_restart).start()
    # ===============================================
    
    # Owner commands
    # ===============================================
    dp.add_handler(CommandHandler(["restart", "r"], restart))
    dp.add_handler(CommandHandler("read", commands.admin.read.init))
    dp.add_handler(CommandHandler("update", commands.admin.update.init))
    
    # Plugins [BETA]
    # ===============================================
    # Covid-19 daily report [BETA]
    dp.add_handler(CommandHandler("covid", plugins.covid19.set_timer,pass_args=False,pass_job_queue=True,pass_chat_data=True))
    dp.add_handler(CommandHandler("uncovid", plugins.covid19.unset, pass_chat_data=True))
    dp.add_handler(CommandHandler("vaccines", plugins.vaccines.set_timer,pass_args=False,pass_job_queue=True,pass_chat_data=True))
    dp.add_handler(CommandHandler("unvaccines", plugins.vaccines.unset, pass_chat_data=True))
    
    # Admin commands
    # ===============================================
    dp.add_handler(CommandHandler("addgroup", commands.admin.addgroup.init))
    dp.add_handler(CommandHandler("delgroup", commands.admin.delgroup.init))

    #User commands
    # ===============================================
    dp.add_handler(CommandHandler("start", commands.user.start.init))
    dp.add_handler(CommandHandler(["help", "aiuto"], commands.user.help.init))
    dp.add_handler(CommandHandler("addme", commands.user.addme.init))
    dp.add_handler(CommandHandler("delme", commands.user.delme.init))
    dp.add_handler(CommandHandler("day", commands.user.covid.init))
    dp.add_handler(CommandHandler("week", commands.user.covidweek.init))
    dp.add_handler(CommandHandler("month", commands.user.covidmonth.init))
    dp.add_handler(CommandHandler("vax", commands.user.vax.init))



    
    # Message Handlers 
    # ===============================================
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, dialogs.welcome.init))    # Welcome
    # ===============================================

    # Display errors and warnings 
    dp.add_error_handler(errors.log.init)              #console log
    dp.add_error_handler(errors.callback_error.init)   #channel log
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
