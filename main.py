import telebot
from telebot import types

bot = telebot.TeleBot("5481244048:AAExLObyLVAMFoYg-tew8OcJ5Ggz_IpEaNA")
#dir = {['genre': size: x:]}

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Поехали")
    markup.add(item1)

    mess = f"Привет, {message.from_user.first_name} , я помогу выбрать аниме которое тебе точно понравится ∩^ω^∩"
    bot.send_message(message.chat.id, mess.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])  # создаем обработчик событий
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Поехали":  # делаем подменю
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mess = f"Давай выберем жанр аниме(o^ ^o)"
            item1 = types.KeyboardButton("Боевик")
            item2 = types.KeyboardButton("Драма")
            item3 = types.KeyboardButton("Детектив")
            item4 = types.KeyboardButton("Ужасы")
            item5 = types.KeyboardButton("Комедия")
            item6 = types.KeyboardButton("Повседневность")
            item7 = types.KeyboardButton("Романтика")
            item8 = types.KeyboardButton("Спокон")
            item9 = types.KeyboardButton("Приключения")
            item10 = types.KeyboardButton("Фэнтези")
            item11 = types.KeyboardButton("Психология")
            item12 = types.KeyboardButton("Этти")
            item13 = types.KeyboardButton("Экшен")
            back = types.KeyboardButton("Меню (♡μ_μ)")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, back)
            bot.send_message(message.chat.id, mess, reply_markup=markup)

 #           dir[genre] =

@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Боевик" or "Драма" or "Детектив" or "Ужасы" or "Комедия" or "Повседневность" or  "Романтика" or "Спокон" or "Приключения" or "Фэнтези" or "Психология" or "Этти" or "Экшен":
            mess = f"Теперь давай определимся с количеством серий づ◡﹏◡)づ"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("12")
            item2 = types.KeyboardButton("24")
            item3 = types.KeyboardButton("24+")
            item4 = types.KeyboardButton("Полнометражное")
            back = types.KeyboardButton("Меню (♡μ_μ)")
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "12" or "24" or "24+" or "Полнометражное":
            mess1 = f"Онгоинг или неважно (^.~)"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Онгоинг")
            item2 = types.KeyboardButton("Неважно")
            back = types.KeyboardButton("Меню (♡μ_μ)")
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, mess1, reply_markup=markup)


bot.polling(none_stop=True)