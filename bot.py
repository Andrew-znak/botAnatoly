import logging, os
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from telegram import Update
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = Updater(token=os.environ.get('BOT_TOKEN'))

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="My name is Tolia and I'm so SAADDD")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)