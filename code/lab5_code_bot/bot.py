import telebot

token = '5004132801:AAF2EX30QuSkgiXf-3CC8MMJ7-97avUjSUs'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Тикитоки', '/Фразочки', 'Пока')
    bot.send_message(message.chat.id, 'Хеллоу!', reply_markup=keyboard)

@bot.message_handler(commands=['Фразочки'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Ну а что говорить?', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Пить сок???', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Дорогу педагогу!', callback_data=5))
    bot.send_message(message.chat.id, text="Выберите, продожение какой фразы вы хотите узнать", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'тикитоки':
        bot.send_message(message.chat.id, 'Лови и кайфуй)')
        bot.send_message(message.chat.id, 'https://www.tiktok.com/t/ZSeftcua4/')
        bot.send_message(message.chat.id, 'https://www.tiktok.com/t/ZSeftoWUn/')
        bot.send_message(message.chat.id, 'https://www.tiktok.com/t/ZSeftXK5E/')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пошла пополнять запас тики-токов!')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветики еще раз')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Выберите, продожение какой фразы вы хотите узнать')
    answer = ''
    if call.data == '3':
        answer = 'Ну а что говорить?.. ' \
                 'Ламинааат!..'
    elif call.data == '4':
        answer = 'Пить сок??? ' \
                 'Пить сок!!!!'
    elif call.data == '5':
        answer = 'Дорогу педагогу, что у нас тут вкусненького?'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()