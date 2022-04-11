#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5236076427:AAH1D8N0riSPm5s6t0gNchWmb612nNhw3cY'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('1.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Git hub")
	item2 = types.KeyboardButton("😋 Написать мне в личку")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет тебе от Евгении и космического кота, друг мой!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Git hub':
			bot.send_message(message.chat.id, 'https://github.com/EvgenyaBond')
		elif message.text == '😋 Написать мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/jeniferbond')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods