import telebot
import random
bot = telebot.TeleBot('5321021406:AAGFKeWH3wtTHXs7FVG44WbLLKYs84RAXkk')

@bot.message_handler(commands=['wtf'])
def wtf(message):
    bot.send_message(message.chat.id, f"Есть команда старт\nЕсть команда help")
@bot.message_handler(commands=['help'])
def description(message):
    bot.send_message(message.chat.id, "Я умный калькулятор и люблю считать циферки")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name + ', я умею считать)))')
@bot.message_handler(func=lambda message: True)
def calc(message):
    try:
        x = message.text
        str = compile(x, 'string', 'eval')
        c = eval(str)
        bot.send_message(message.chat.id, f"{message.text} = {c}")
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'На ноль делить нельзя')
    except SyntaxError:
        bot.send_message(message.chat.id, 'Я понимаю только цифры')
    except NameError:
        bot.send_message(message.chat.id, random.choice(seq=[('Я понимаю только цифры'), ("Я тебя не понял"), ("Ты о чем?")]))
bot.polling(none_stop=True)

