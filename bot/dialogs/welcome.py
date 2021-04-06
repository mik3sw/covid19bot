import config
import functions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def init(update, context):

	for new in update.message.new_chat_members:
		if str(new.username).lower() == config.bot_username:
			txt = functions.general.txtReader('welcome')
			context.bot.send_message(update.message.chat_id, text=txt, parse_mode='HTML')