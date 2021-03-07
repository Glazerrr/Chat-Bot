import telebot
import pandas as pd

document_text = open('info.csv', 'r')
text_string = document_text.read().lower()
df = pd.read_csv('info.csv', delimiter=';', encoding='1251')
bot = telebot.TeleBot('1694618937:AAF1ZWyYK5fuHcUIZx8CGRCyGtDEsBlPxqY')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Места', 'Прочее')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Количество бюджетных мест', 'Количество целевых мест', 'Количество квотных мест',
              'Количество платных мест', 'Назад')
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('Цена за обучение', 'Какие экзамены нужно сдавать?', 'Назад')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                     f'Я бот для абитуриентов ПетрГУ. Приятно познакомиться, {message.from_user.first_name}',
                     reply_markup=keyboard1)


# @bot.message_handler(commands=['help'])
# def help_message(message):
#     bot.reply_to(message, 'бюджетные места у %номер направления без точек% - количество бюджетных мест')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Места':
        bot.send_message(message.from_user.id, 'Выберите интересующее вас меню', reply_markup=keyboard2)
    if message.text == 'Прочее':
        bot.send_message(message.from_user.id, 'Выберите интересующее вас меню', reply_markup=keyboard3)
    if message.text == 'Количество бюджетных мест':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_budget)
    if message.text == 'Количество целевых мест':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_target)
    if message.text == 'Количество платных мест':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_paid)
    if message.text == 'Количество квотных мест':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_q)
    if message.text == 'Назад':
            bot.send_message(message.from_user.id, 'Выберите интересующее вас меню', reply_markup=keyboard1)
    if message.text == 'Цена за обучение':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_cost)
    if message.text == 'Какие экзамены нужно сдавать?':
            bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
            bot.register_next_step_handler(message, get_code_exam)
    if message.text == 'Пиздец':
            bot.send_message(message.from_user.id, 'Я знаю....')


def get_code_budget(message):
    global code
    try:
        code = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    code = int(message.text.lower())
    a = df[df['Код'] == code]
    bot.send_message(message.from_user.id,
                     'Количество бюджетных мест на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                         a['Бюдж'].values.item()))
    bot.register_next_step_handler(message, get_text_messages)


def get_code_target(message):
        global code
        try:
            code = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        code = int(message.text.lower())
        a = df[df['Код'] == code]
        bot.send_message(message.from_user.id,
                         'Количество целевых мест на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                             a['Целевик'].values.item()))
        bot.register_next_step_handler(message, get_text_messages)


def get_code_paid(message):
        global code
        try:
            code = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        code = int(message.text.lower())
        a = df[df['Код'] == code]
        bot.send_message(message.from_user.id,
                     'Количество платных мест на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                         a['Плат'].values.item()))
        bot.register_next_step_handler(message, get_text_messages)


def get_code_q(message):
        global code
        try:
            code = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        code = int(message.text.lower())
        a = df[df['Код'] == code]
        bot.send_message(message.from_user.id,
                     'Количество квотных мест на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                         a['Квота'].values.item()))
        bot.register_next_step_handler(message, get_text_messages)


def get_code_cost(message):
    global code
    try:
        code = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    code = int(message.text.lower())
    a = df[df['Код'] == code]
    bot.send_message(message.from_user.id,
                     'Цена за обучение на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                         a['Цена'].values.item()))
    bot.register_next_step_handler(message, get_text_messages)


def get_code_exam(message):
    global code
    try:
        code = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    code = int(message.text.lower())
    a = df[df['Код'] == code]
    bot.send_message(message.from_user.id,
                     'Необходимые экзамены на направлении ' + str(a['Название'].values.item()) + ': ' + str(
                         a['Экз'].values.item()))
    bot.register_next_step_handler(message, get_text_messages)


bot.polling(none_stop=True)
