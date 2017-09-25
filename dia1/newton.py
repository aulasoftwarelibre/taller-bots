#!/usr/bin/env python
# coding=utf-8

import logging
import requests
import telebot
from config import TOKEN

COMMANDS = [
    'simplify',
    'factor',
    'derive',
    'integrate',
    'zeroes'
    'tangent',
    'area',
    'cos',
    'sin',
    'tan',
    'arccos',
    'arcsin',
    'arctan',
    'abs',
    'log',
]

bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.DEBUG)


def newton_api(operation, expression):
    url = "https://newton.now.sh/{}/{}".format(operation, expression)
    telebot.logger.info('Connection: {} {}'.format(operation, expression))

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    raise ValueError('Problema al conectar con el servidor (Error {}).'.format(r.status_code))


@bot.message_handler(commands=COMMANDS)
def simplify(message):
    """Responde a una petición de cálculo. Las órdenes disponibles son:

    simplify  - Simplify
    factor    - Factor
    derive    - Derive
    integrate - Integrate
    zeroes    - Find
    tangent   - Find Tangent
    area      - Area Under
    cos       - Cosine
    sin       - Sine
    tan       - Tangent
    arccos    - Inverse Cosine
    arcsin    - Inverse Sine
    arctan    - Inverse Tangent
    abs       - Absolute Value
    log       - Logarithm

    :param message: telebot.types.Message
    :return: None
    """
    command = telebot.util.extract_command(message.text)
    expression = telebot.util.extract_arguments(message.text)

    if expression:
        result = newton_api(command, expression)

        bot.send_message(message.chat.id, "Resultado: {}".format(result['result']))
    else:
        bot.send_message(message.chat.id, "Debe indicar una expresión")


bot.polling()
