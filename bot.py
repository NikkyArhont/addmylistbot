from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция, которая вызывается, когда пользователь отправляет команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправь мне список покупок, и я помогу тебе его отслеживать.')

# Основная функция для запуска бота
def main():
    updater = Updater("7957963695:AAFrJnlLAavXFmv7LOTh2oVC0Kj2sglDgdY", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
