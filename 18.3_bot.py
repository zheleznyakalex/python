import telebot

bot = telebot.TeleBot ("1518658094:AAELByIW29SpLDokdWCb7dU1Dk99dVq8rSo")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler (commands=['start', 'help'],content_types=['photo', ])
def repeat(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f'Приветствую, {message.chat.username}')

def say_lmao(message: telebot.types.Message):
    bot.reply_to (message, 'Nice meme XDD')

bot.polling(none_stop=True)