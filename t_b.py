import telebot

# Вставьте сюда ваш токен от бота
API_TOKEN = '7662312242:AAFh2_ZenW8krULF-nCMn1bl7sGnxTP2hm0'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.reply_to(message, "Привет. И тебе всего хорошего!!!")

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки сообщений
    bot.polling()
