import telebot
from telebot import types

# Your token
TOKEN = '7458394978:AAEIg7G200HOROPmLWOe53ON8BzkGf6CLVw'
# Your personal Telegram ID
YOUR_TELEGRAM_ID = '476101958'

bot = telebot.TeleBot(TOKEN)

# Dictionary to store user data
user_data = {}

# Counters for the sequential user numbers
first_time_counter = 0
repeat_counter = 0

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Бори аввал')
    btn2 = types.KeyboardButton('Такроран')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Салом, лутфан интихоб намоед!:", reply_markup=markup)

# Handler for button presses
@bot.message_handler(func=lambda message: message.text in ['Бори аввал', 'Такроран'])
def handle_buttons(message):
    user_data[message.chat.id] = {'step': 1, 'type': message.text}
    bot.send_message(message.chat.id, "Рақами Телефони худро ворид намоед:")

# Handler for phone number input
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 1)
def handle_phone(message):
    user_data[message.chat.id]['phone'] = message.text
    user_data[message.chat.id]['step'] = 2
    bot.send_message(message.chat.id, "Лутфан Ному насаби худро нависед:")

# Handler for name input
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('step') == 2)
def handle_name(message):
    global first_time_counter, repeat_counter
    user_data[message.chat.id]['name'] = message.text
    user_data[message.chat.id]['step'] = 3

    if user_data[message.chat.id]['type'] == 'Бори аввал':
        first_time_counter += 1
        next_number = first_time_counter
    else:
        repeat_counter += 1
        next_number = repeat_counter

    # Send data to your personal account
    message_text = f"Номер: {next_number}\nНому насаб: {user_data[message.chat.id]['name']}\nТелефон: {user_data[message.chat.id]['phone']}\nТип: {user_data[message.chat.id]['type']}"
    bot.send_message(YOUR_TELEGRAM_ID, message_text)

    # Notify the user of their registration number
    bot.send_message(message.chat.id, f"Навбати Шумо: {next_number} ({user_data[message.chat.id]['type']})")

    # Clear user data for this chat ID
    del user_data[message.chat.id]

# Start the bot
bot.polling()
