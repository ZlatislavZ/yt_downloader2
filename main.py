import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
from pytube import YouTube
from decouple import config

# Load the bot token from the environment variable
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your YouTube downloader bot. Send me a YouTube link, and I'll download the video.")

# Define a function to handle YouTube links
def download_youtube(update: Update, context: CallbackContext):
    url = update.message.text
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download()

    # Respond with a message indicating successful download
    update.message.reply_text("Video downloaded successfully!")

def main():
    # Initialize the Telegram Bot
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_youtube))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
