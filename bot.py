import logging, os
import image, phrases

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

"""
def start(update: Update, context: CallbackContext) -> None:
    Send a message when the command /start is issued
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
"""

def get_image(update: Update, context: CallbackContext) -> None:
    """Download image to the bytearray"""
    file = context.bot.get_file(update.message.photo[-1].file_id).download_as_bytearray()
    final_image = (image.change_image(file))
    context.bot.send_photo(chat_id=update.message.chat_id,photo=final_image.getvalue())

def get_reply_image(update: Update, context: CallbackContext) -> None:
    """Download replied image to bytearray"""
    file = context.bot.get_file(update.message.reply_to_message.photo[-1].file_id).download_as_bytearray()
    final_image = (image.change_image(file))
    context.bot.send_photo(chat_id=update.message.chat_id,photo=final_image.getvalue())

def main() -> None:
    updater = Updater(os.environ['BOT_TOKEN'])
    dispatcher = updater.dispatcher
    phrases.read_phrases()
    dispatcher.add_handler(MessageHandler(Filters.photo & Filters.caption_regex(r'^[Тт]олик$'), get_image))
    dispatcher.add_handler(MessageHandler((Filters.reply & Filters.regex(r'^[Тт]олик$')), get_reply_image))
    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()