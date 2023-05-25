from telebot import TeleBot, types
from get_calebration import get_celebration, get_CelDay
from re import match

token = "5979518808:AAGmnFp_MNCwMFzEfpYEyhyIE5pQV_OL6Xs"

bot = TeleBot(token)

@bot.message_handler(commands = ["start"])
def welcome(message):
    "Приветствие и активация конпок"
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) 
    item1 = types.KeyboardButton("Узнать праздники на определенный день.")
    item2 = types.KeyboardButton("Узнать праздники на сегодня.")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет! Я бот, который перечислит тебе все\
    празданики дня. Просто нажми на кнопку 'Узнать праздники на сегодня.'", reply_markup = markup) 


@bot.message_handler(content_types = ["text"])
def take_over_handler(message):
    if message.text == "Узнать праздники на определенный день.":
        bot.register_next_step_handler(message, give_holiday)
        answer = "Отлично! Теперь укажи дату проведения праздников в формате дд.мм. Например: 01.11"
    elif message.text == "Узнать праздники на сегодня.":
        answer = get_celebration()
    else:
        answer = "Я вас не понял. Нажмите на кнопку 'Узнать праздники на определенный день.'\
        или 'Узнать праздники на сегодня.'  "
    bot.send_message(message.chat.id, answer)

def give_holiday(message):
    "Выдает праздники дня"
    holiday = get_CelDay(message.text) if match(r"\d{2}.\d{2}", message.text) else None
    if holiday:
        result = ''.join(i for i in holiday)
        bot.send_message(message.chat.id, result)
    elif message.text == "Узнать праздники на определенный день." or message.text == "Узнать праздники на сегодня.":
        take_over_handler(message)
    else:
        bot.send_message(message.chat.id, f"Неверно набрана дата. Попробуйте снова.")
        bot.register_next_step_handler(message, give_holiday)

bot.polling(non_stop = True, interval = 0)
