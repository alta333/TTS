import pyttsx3
import telebot
from telebot import types

engine = pyttsx3.init()
voices = engine.getProperty('voices')

voice = 'Aleksandr'

engine.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Elena':
        engine.setProperty('voice', voice.id)

bot = telebot.TeleBot('2038731907:AAGyVFyv2NcmGWkBfVgKEi8GuuW-d2vyTlA') #2108679679:AAHTPdSd-RpnxvvMrUomZ5XSxJsS2fQssNU

@bot.message_handler(commands=['start'])
def welcome(message):
    print(f"{message.chat.first_name} ({message.chat.username}): {message.text}")
    bot.send_message(message.chat.id,f"Добро пожаловать, {message.chat.first_name}!\n"
                                     f"Я - TextToAudioByKirillBot, бот созданный чтобы озвучивать текст который ты напишеш в чат.\n"
                                     f"Также ты можеш сменить голос и громкость /settings\n\n"
                                     f"P.S. Мой разроботчик Кирилл")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item2)




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(f"{message.chat.first_name} ({message.chat.username}): {message.text}")

    if message.text == "/help":
        bot.send_message(message.from_user.id, f"Напишите мне текст, а я его озвучю!\nТакже ты можеш сменить голос и громкость /settings")

    if message.text == "/settings":

        markup = types.InlineKeyboardMarkup(row_width=2)
        Aleksandr = types.InlineKeyboardButton("Aleksandr", callback_data='Aleksandr')
        Elena = types.InlineKeyboardButton("Elena", callback_data='Elena')
        Irina = types.InlineKeyboardButton("Irina", callback_data='Irina')
        #Volem = types.InlineKeyboardButton(Volem_, callback_data='Irina')

        markup.add(Aleksandr, Elena, Irina)
        bot.send_message(message.chat.id,
                         f"Сейчас установлен голос: {voice.name}\nВыбери голос:".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)


        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "Aleksandr":
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Установлен голос: Aleksandr")
                for voice in voices: 
                    if voice.name == 'Aleksandr':
                        engine.setProperty('voice', voice.id)

            if call.data == "Elena":
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Установлен голос: Elena")
                engine.setProperty('voice', 'ru')
                for voice in voices: 
                    if voice.name == 'Elena':
                        engine.setProperty('voice', voice.id)

            if call.data == "Irina":
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Установлен голос: Irina")
                engine.setProperty('voice', 'ru')
                for voice in voices:
                    if voice.name == 'Irina':
                        engine.setProperty('voice', voice.id)
    else:

        engine.save_to_file(message.text, 'audio.mp3') #
        engine.runAndWait()
        with open("audio.mp3", "rb") as misc:
            f = misc.read()

        bot.send_audio(message.chat.id, f)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Брось кубик':
            bot.send_message(message.chat.id, "sa")
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')




if __name__ == '__main__':
     bot.infinity_polling()

#bot.send_message(message.chat.id, message.text)
