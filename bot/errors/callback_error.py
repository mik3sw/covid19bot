from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
import config
import logging


def init(update, context):
    err = '[error]'
    try:
        raise context.error
    except Unauthorized:
        err = '[ERROR] Unauthorized\n'
        #error_message(update, context, err)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        err = '[ERROR] BadRequest - malformed requests\n'
        #error_message(update, context, err)
        # handle malformed requests - read more below!
    except TimedOut:
        err = '[ERROR] TimedOut - slow connection problems\n'
        #error_message(update, context, err)
        # handle slow connection problems
    except NetworkError:
        err = '[ERROR] NetworkError - other connection problems\n'
        #error_message(update, context, err)
        # handle other connection problems
    except ChatMigrated:
        err = '[ERROR] ChatMigrated - chat_id not found (maybe group/channel migrated?)\n'
        #error_message(update, context, err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        err = '[ERROR] TelegramError\nThis is a generic error not handled by other handlers, check the console logs for info\n'
        #error_message(update, context, err)
        # handle all other telegram related errors
    except AttributeError:
        err = '[ERROR] AttributeError -  bad code'
    finally:
        error_message(update, context, err)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error_message(update, context, err):
    log = '\n[LOG] errore: {}'.format(context.error)
    context.bot.send_message(chat_id=config.log_channel, text = err+log, parse_mode='HTML')