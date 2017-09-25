#!/usr/bin/env python
# coding=utf-8

import logging
import telebot
from random import randint
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.DEBUG)

user_dict = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Adivina el número (del 1 al 100)")
    user_dict[chat_id] = randint(1, 100)

    bot.register_next_step_handler(msg, guest_number)


def guest_number(message):
    chat_id = message.chat.id

    if not message.text.isdigit():
        msg = bot.send_message(chat_id, "Eso no es un número")
        bot.register_next_step_handler(msg, guest_number)
        return

    number = int(message.text)
    number_to_guess = user_dict[chat_id]

    if number == number_to_guess:
        bot.send_message(chat_id, "Enhorabuena, esa era el número")
        return

    if number < number_to_guess:
        msg = bot.send_message(chat_id, "Demasiado pequeño")
        bot.register_next_step_handler(msg, guest_number)
        return

    msg = bot.send_message(chat_id, "Demasiado grande")
    bot.register_next_step_handler(msg, guest_number)


bot.polling()
