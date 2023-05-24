from telebot import TeleBot, types
from get_calebration import get_celebration

token = "5979518808:AAGmnFp_MNCwMFzEfpYEyhyIE5pQV_OL6Xs"

bot = TeleBot(token)

@bot.message_handler(commands = ["start"])
def welcome(message):
    "Приветствие и активация конпок"
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) 
    item1 = types.KeyboardButton("Что я умею?")
    item2 = types.KeyboardButton("Узнать праздники дня.")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет! Я бот, который перечислит тебе все\
    празданики дня. Просто нажми на кнопку 'Узнать праздники дня.'", reply_markup = markup) 


@bot.message_handler(content_types = ["text"])
def take_over_handler(message):
    if message.text == "Узнать праздники дня.":
        bot.register_next_step_handler(message, give_holiday)
        answer = "Отлично! Теперь укажи дату проведения праздников в формате дд.мм.гг"
    elif message.text == "Что я умею?":
        answer = "Я умею перечислять праздники дня.\
    Просто нажми на кнопку 'Узнать праздники дня.' и укажи дату проведения праздников."
    else:
        answer = "Я вас не понял. Нажмите на кнопку 'Что я умею?'"
    bot.send_message(message.chat.id, answer)

def give_holiday(message):
    "Выдает праздники дня"
    result = ''.join(i for i in get_celebration())
    bot.send_message(message.chat.id, f"Вот все праздники на {message.text}:\n{result}")

bot.polling(non_stop = True, interval = 0)
