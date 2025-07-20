import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧴 Продукты")
    btn2 = types.KeyboardButton("🎁 Акции")
    btn3 = types.KeyboardButton("📝 Как зарегистрироваться")
    btn4 = types.KeyboardButton("📞 Связаться с консультантом")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, "Добро пожаловать в мир здоровья с Siberian Wellness! Выберите раздел:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def respond(message):
    if message.text == "🧴 Продукты":
        bot.send_message(message.chat.id, "🌿 Ознакомьтесь с каталогом продуктов на сайте:\nhttps://kg.siberianhealth.com/ru/")
    elif message.text == "🎁 Акции":
        bot.send_message(message.chat.id, "🎉 Актуальные акции:\nhttps://kg.siberianhealth.com/ru/shop/actions/")
    elif message.text == "📝 Как зарегистрироваться":
        bot.send_message(message.chat.id, "Чтобы зарегистрироваться:\n1. Перейдите на сайт: https://kg.siberianhealth.com/\n2. Нажмите 'Регистрация'\n3. Заполните анкету\n4. Укажите ID вашего консультанта (если есть)")
    elif message.text == "📞 Связаться с консультантом":
        bot.send_message(message.chat.id, "📲 Вы можете написать вашему консультанту или в службу поддержки:\nEmail: support@siberianwellness.com\nТелефон: +996 *** *** ***")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите действие из меню.")

bot.polling(none_stop=True)
