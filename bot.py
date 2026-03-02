import telebot
from telebot import types
import os

# 🔒 Токен берется из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

user_messages = {}

# ---------- МЕНЮ ----------

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💰 Кэшбек, скидки и подарки", callback_data="cooperation"),
        types.InlineKeyboardButton("🎁 Акции", callback_data="promotions")
    )
    markup.add(
        types.InlineKeyboardButton("📍 Контактная информация", callback_data="contacts"),
        types.InlineKeyboardButton("🧬 Тест NUTRITION FITCHA", callback_data="nutrition_fitcha")
    )
    markup.add(
        types.InlineKeyboardButton("🔄 Перезагрузка бота", callback_data="start_virtual")
    )
    return markup


def promo_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📅 Недельные акции", callback_data="promo_week"),
        types.InlineKeyboardButton("🗓 Месячные акции", callback_data="promo_month")
    )
    markup.add(
        types.InlineKeyboardButton("⬅️ Назад", callback_data="back_main")
    )
    markup.add(
        types.InlineKeyboardButton("🔄 Перезагрузка бота", callback_data="start_virtual")
    )
    return markup

# ---------- СЛУЖЕБНЫЕ ФУНКЦИИ ----------

def clear_chat(chat_id):
    if chat_id in user_messages:
        for msg_id in user_messages[chat_id]:
            try:
                bot.delete_message(chat_id, msg_id)
            except:
                pass
        user_messages[chat_id] = []


def send_media_group(chat_id, photos, caption):
    clear_chat(chat_id)

    media = [types.InputMediaPhoto(photo) for photo in photos]
    messages = bot.send_media_group(chat_id, media)

    user_messages[chat_id] = [m.message_id for m in messages]

    msg = bot.send_message(chat_id, caption, reply_markup=promo_menu())
    user_messages[chat_id].append(msg.message_id)

# ---------- START ----------

@bot.message_handler(commands=['start'])
def start(message):
    clear_chat(message.chat.id)

    msg = bot.send_message(
        message.chat.id,
        "Добро пожаловать в мир здоровья с Siberian Wellness!\n"
        "Выберите раздел ниже 👇\n\n"
        "💬 Или просто отправьте /start в чат, чтобы начать заново.",
        reply_markup=main_menu()
    )

    user_messages[message.chat.id] = [msg.message_id]

# ---------- CALLBACK ----------

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    # ❗ ОБЯЗАТЕЛЬНО подтверждаем callback
    bot.answer_callback_query(call.id)

    if not call.message:
        return

    chat_id = call.message.chat.id

    try:
        if call.data == "start_virtual":
            clear_chat(chat_id)
            msg = bot.send_message(
                chat_id,
                "🔄 Перезапуск бота...\n\n"
                "Добро пожаловать в мир здоровья с Siberian Wellness!\n"
                "Выберите раздел ниже 👇\n\n"
                "💬 Или просто отправьте /start в чат, чтобы начать заново.",
                reply_markup=main_menu()
            )
            user_messages[chat_id] = [msg.message_id]

        elif call.data == "cooperation":
            clear_chat(chat_id)

            photo_msg = bot.send_photo(
                chat_id,
                "https://i.postimg.cc/yN8W5MQc/photo-2025-10-30-00-15-22.jpg"
            )

            msg = bot.send_message(
                chat_id,
                "💰 Кэшбек, скидки и подарки Siberian Wellness!\n"
                "Получайте бонусы, скидки и подарки за покупки.\n\n"
                "🔗 Регистрация:\n"
                "https://kg.siberianhealth.com/ru/shop/user/registration/PRIVILEGED_CLIENT/?referral=6752908\n\n"
                "💬 Или просто отправьте /start в чат, чтобы начать заново.",
                reply_markup=main_menu()
            )

            user_messages[chat_id] = [photo_msg.message_id, msg.message_id]

        elif call.data == "nutrition_fitcha":
            clear_chat(chat_id)

            msg = bot.send_message(
                chat_id,
                "🧬 NUTRITION FITCHA — тест для подбора витаминов\n\n"
                "Автоматизированный сервис подбора витаминов и микронутриентов.\n\n"
                "🔗 Пройти тест:\n"
                "https://ru.siberianhealth.com/ru/fitcha/nutrilogic/\n\n"
                "💬 Или просто отправьте /start в чат, чтобы начать заново.",
                reply_markup=main_menu()
            )

            user_messages[chat_id] = [msg.message_id]

        elif call.data == "promotions":
            clear_chat(chat_id)

            msg = bot.send_message(
                chat_id,
                "🎁 Выберите категорию акций:",
                reply_markup=promo_menu()
            )

            user_messages[chat_id] = [msg.message_id]

        elif call.data == "contacts":
            clear_chat(chat_id)

            msg = bot.send_message(
                chat_id,
                "📞 Телефоны:\n"
                "0550 724 280\n0555 945 794\n0558 995 985\n\n"
                "🏢 Адрес:\n"
                "ул. Суеркулова 8/3,\n"
                "при клинике «Семья и здоровье», первое крыльцо\n\n"
                "🗺 Карта:\nhttps://go.2gis.com/qukcy\n\n"
                "💬 Или просто отправьте /start в чат, чтобы начать заново.",
                reply_markup=main_menu()
            )

            user_messages[chat_id] = [msg.message_id]

        elif call.data == "promo_week":
            photos_week = [
                "https://i.postimg.cc/yd4GJTb8/Whats-App-Image-2026-03-02-at-13-43-20.jpg"
            ]

            send_media_group(
                chat_id,
                photos_week,
                "📅 Недельные акции Siberian Wellness 🌿"
            )

        elif call.data == "promo_month":
            photos_month = [
                "https://i.postimg.cc/vTM2HHSv/Whats-App-Image-2026-03-02-at-13-43-33.jpg",
                "https://i.postimg.cc/vHY2JTn9/Whats-App-Image-2026-03-02-at-13-43-33-(1).jpg"
            ]

            send_media_group(
                chat_id,
                photos_month,
                "🗓 Месячные акции Siberian Wellness 🎉"
            )

        elif call.data == "back_main":
            clear_chat(chat_id)

            msg = bot.send_message(
                chat_id,
                "Добро пожаловать в главное меню 👇\n\n"
                "💬 Или просто отправьте /start в чат, чтобы начать заново.",
                reply_markup=main_menu()
            )

            user_messages[chat_id] = [msg.message_id]

    except Exception as e:
        print("⚠️ Ошибка:", e)

# ---------- RUN ----------

if __name__ == "__main__":
    print("🤖 Бот запущен и слушает команды...")
    bot.polling(none_stop=True, interval=0, timeout=20)






