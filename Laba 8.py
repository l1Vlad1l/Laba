import telebot

from nedelya import curr_week_for_bd, curr_week
from bd import get_day_formatting, get_week_formatting
from telebot import TeleBot

token = '5954290497:AAFleDDC0qhO2VFOcf7di6W1Ni0RtvpcTAQ'
bot: TeleBot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}! Я бот для отображения информации о"
                                           " расписании. Напишите /help, я обьясню вам, как я работаю"
                     .format(message.from_user))


@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.send_message(message.chat.id, text='Напишите /week - для того, чтобы узнать, какая сейчас неделя\nНапишите '
                                           '/mtuci - для того, чтобы попасть на сайт МТУСИ\nУ меня есть такие '
                                           'команды:'
                                           '/monday, /tuesday, /wednesday, /thursday, /friday, /satturday, '
                                           '/currentweek, /nextweek')


@bot.message_handler(commands=['week'])
def help_bot(message):
    bot.send_message(message.chat.id, text=f'Сейчас {curr_week()} неделя')


@bot.message_handler(commands=['mtuci'])
def help_bot(message):
    bot.send_message(message.chat.id, text='Сайт МТУСИ: https://mtuci.ru')


@bot.message_handler(commands=['monday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 1))}', parse_mode='HTML')


@bot.message_handler(commands=['tuesday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 2))}', parse_mode='HTML')


@bot.message_handler(commands=['wednesday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 3))}', parse_mode='HTML')


@bot.message_handler(commands=['thursday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 4))}', parse_mode='HTML')


@bot.message_handler(commands=['friday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 5))}', parse_mode='HTML')


@bot.message_handler(commands=['satturday'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_day_formatting(curr_week_for_bd(0), 6))}', parse_mode='HTML')


@bot.message_handler(commands=['currentweek'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(commands=['nextweek'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{str(get_week_formatting(curr_week_for_bd(1)))}', parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, text='Я вас не понимаю')


bot.polling(none_stop=True, interval=0)