import telebot
import random
from telebot.types import  Message

TOKEN = "987421062:AAFVAT7C88Kt5GXsA8timpjl9dVkWdFvj5I"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
	bot.reply_to(message,'hello bro')



@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
	if 'ppp' in message.text:
		bot.reply_to(message, 'hi')
		return

	bot.reply_to(message, str(random.random()))




bot.polling()
