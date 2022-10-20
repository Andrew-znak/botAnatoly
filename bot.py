from asyncore import read
import logging, os

from io import BytesIO
from tabnanny import filename_only
from PIL import Image, ImageFont, ImageDraw 
from telegram import Update, ForceReply, File
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def get_image(update: Update, context: CallbackContext) -> None:
    """Download image to the bytearray"""
    file = context.bot.get_file(update.message.photo[-1].file_id)
    f = BytesIO(file.download_as_bytearray())
    final_image = (change_image(f))
    context.bot.send_photo(chat_id=update.message.chat_id,photo=final_image.getvalue())


def change_image(img: BytesIO):
    """Add text to the image"""
    image = Image.open(img)
    img_byte_array = BytesIO()
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    title_text = "Я Толик и мне очень грустно"
    image_editable = ImageDraw.Draw(image)
    image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    image.save(img_byte_array, format='JPEG')
    return img_byte_array
    

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ['BOT_TOKEN'])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler((Filters.reply & Filters.regex(r'^[Тт]олик$')) | (Filters.photo & Filters.caption_regex(r'^[Тт]олик$')) , get_image))
    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()