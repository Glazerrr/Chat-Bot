import telebot
import pandas as pd

document_text = open('info.csv', 'r')
text_string = document_text.read().lower()
df = pd.read_csv('info.csv', delimiter=';', encoding='1251')
bot = telebot.TeleBot('1694618937:AAF1ZWyYK5fuHcUIZx8CGRCyGtDEsBlPxqY')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Количество бюджетных мест', 'Количество целевых мест', 'Количество квотных мест',
              'Количество платных мест', 'Цена за обучение', 'Какие экзамены нужно сдавать?')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Я бот. Приятно познакомиться, {message.from_user.first_name}',
                     reply_markup=keyboard1)


# @bot.message_handler(commands=['help'])
# def help_message(message):
#     bot.reply_to(message, 'бюджетные места у %номер направления без точек% - количество бюджетных мест')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Количество бюджетных мест':
        bot.send_message(message.from_user.id, 'Введите номер направления без точек и пробелов')
        bot.register_next_step_handler(message, get_code)


def get_code(message):
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


bot.polling(none_stop=True)
