import os
import re
from modules.valo_image import getImg
from modules.valo_data import getData
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = os.environ.get('TG_TOKEN')
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


def start(update, _):
    update.message.reply_text('Use "/valo <username#tagline>" to get stats.')


def valo(update, context):
    context.bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    name = re.sub(r'\/\w+\s', '', update.effective_message.text)
    data = getData(name)
    if isinstance(data, dict):
        update.message.reply_photo(getImg(data))
    else:
        update.message.reply_text(data)


dispatcher.add_handler(CommandHandler('start', start, run_async=True))
dispatcher.add_handler(CommandHandler('valo', valo, run_async=True))

updater.start_polling()
updater.idle()
