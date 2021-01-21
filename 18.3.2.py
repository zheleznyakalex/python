import telebot

bot = telebot.TeleBot ("1518658094:AAELByIW29SpLDokdWCb7dU1Dk99dVq8rSo")


@bot.message_handler (content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to (message, 'Nice meme XDD')

def repeat(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f'Приветствую, {message.chat.username}')


bot.polling (none_stop=True)