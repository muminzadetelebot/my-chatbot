from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Вставьте ваш токен API здесь
API_TOKEN = '7119687473:AAHPAgng_jKj1QKN4biqhNfjuW1MCbWx94M'

# Функция для старта
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Здравствуйте! Я бот для управления очередью пациентов. Отправьте команду /join, чтобы занять очередь.')

# Функция для добавления пациента в очередь
queue = []

def join_queue(update: Update, context: CallbackContext):
    user = update.message.from_user
    queue.append(user.id)
    update.message.reply_text(f'{user.first_name}, вы добавлены в очередь. Ваш номер: {len(queue)}')

# Функция для отображения очереди
def show_queue(update: Update, context: CallbackContext):
    if not queue:
        update.message.reply_text('Очередь пуста.')
    else:
        queue_list = '\n'.join([str(i+1) + '. ' + context.bot.get_chat(user_id).first_name for i, user_id in enumerate(queue)])
        update.message.reply_text(f'Очередь:\n{queue_list}')

# Основная функция для запуска бота
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('join', join_queue))
    dp.add_handler(CommandHandler('queue', show_queue))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
