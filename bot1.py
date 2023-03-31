import telebot
import pickle

# создаем бота и указываем его токен
bot = telebot.TeleBot('6248292082:AAE7axnGamhuXVxhYasZ2QTdXM1wKuM2Fos')

# загружаем данные о пользователях из файла (или создаем пустой словарь, если файла нет)
try:
    with open('users.pickle', 'rb') as f:
        users = pickle.load(f)
except FileNotFoundError:
    users = {}

# обрабатываем новые сообщения
@bot.message_handler(func=lambda message: True)
def echo(message):
    chat_id = message.chat.id
    text = message.text

    # добавляем информацию о пользователе в словарь (если ее еще нет)
    if chat_id not in users:
        users[chat_id] = {
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
            'messages': []
        }

    # добавляем сообщение пользователя в информацию о нем
    users[chat_id]['messages'].append(text)

    # отправляем пользователю его же сообщение
    bot.send_message(chat_id, text)

    # сохраняем данные о пользователях в файл
    with open('users.pickle', 'wb') as f:
        pickle.dump(users, f)

# запускаем бота
bot.polling(none_stop=True, interval=0)

