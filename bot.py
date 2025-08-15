import telebot
from telebot import types
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤝 Сотрудничество")
    btn2 = types.KeyboardButton("🧴 Продукты")
    btn3 = types.KeyboardButton("🎁 Акции")
    btn4 = types.KeyboardButton("📍 Контактная информация")
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4)
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в мир здоровья с Siberian Wellness! Выберите раздел:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def respond(message):
    if message.text == "🧴 Продукты":
        bot.send_message(message.chat.id, "🌿 Ознакомьтесь с каталогом продуктов на сайте:\nhttps://kg.siberianhealth.com/ru/")
    elif message.text == "🎁 Акции":
        bot.send_message(message.chat.id, "🎉 Актуальные акции:\nhttps://kg.siberianhealth.com/ru/shop/actions/")
    elif message.text == "📍 Контактная информация":
        bot.send_message(message.chat.id,
            "📞 Телефоны:\n"
            "0550 724 280\n0555 945 794\n0558 995 985\n\n"
            "🏢 Адрес:\n"
            "ул. Суеркулова 8/3,\nпри клинике «Семья и здоровье»,\nпервое крыльцо\n\n"
            "🗺️ Карта:\nhttps://go.2gis.com/qukcy"
        )
    elif message.text == "🤝 Сотрудничество":
        bot.send_message(message.chat.id,
            "💼 Хочешь зарабатывать вместе с Siberian Wellness?\n"
            "Стань партнёром бренда, развивай свой онлайн-бизнес, получай бонусы и поддержку.\n\n"
            "📲 Присоединяйся по ссылке:\n"
            "https://kg.siberianhealth.com/ru/shop/user/registration/PRIVILEGED_CLIENT/?referral=6752908"
        )
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите действие из меню.")

bot.polling(none_stop=True)

