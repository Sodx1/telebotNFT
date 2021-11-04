
import telebot
import os
import random

bot = telebot.TeleBot("2073524856:AAF2f1WG6KFbk2miul3n6wGHP4dmIqMsqAY")

def log(message, answer):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))

@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)  # переменная, которая хранит разметку нашей клавиатуры
    # 1 - True - для того,чтобы сделать размер клавиатуры поменьше, False - побольше
    # 2 - True - убрать клавиатуру после одного раза пользования
    user_markup.row('Профиль', 'Статистика','О разработчике')  # добавляем команды
    user_markup.row('Покупка цифрового рисунка', 'Покупка звука', 'Покупка видео')# и ограничиваем размер клавиатуры 3х4
    # перед тем, как показать клавиатуру пользователю бот должен отправить сообщение вроде приветствия
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Покупка цифрового рисунка':
        bot.send_message(message.from_user.id,"Вы купили мем за 500 ETH")
        directory = 'C:/cats'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory+'/'+random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img, parse_mode="HTML")
        img.close()
    elif message.text == 'Покупка звука':
        bot.send_message(message.from_user.id,"Вы купили звук за 100 ETH")
        directory = 'C:/audio'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        sound = open(directory+'/'+random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_audio')
        bot.send_audio(message.from_user.id,sound, parse_mode="HTML")
        sound.close()
    elif message.text == 'Покупка видео':
        bot.send_message(message.from_user.id,"Вы купили видео за 200 ETH")
        directory = 'C:/video'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        video = open(directory+'/'+random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_video')
        bot.send_video(message.from_user.id,video, parse_mode="HTML")
        video.close()
    elif message.text == 'Статистика':
        directory = 'C:/rus'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory+'/'+random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img, parse_mode="HTML")
        img.close()
    elif message.text == 'Профиль':
        directory = 'C:/dolg'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory+'/'+random_file,'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img, parse_mode="HTML")
        img.close()
    elif message.text == 'О разработчике':
          bot.send_message(message.from_user.id,"Версия 0.0.1(Демо). Создатель не несет ответственность за проявленные действии в боте! Создатель просто любит мемы :)")

bot.polling(none_stop=True, interval=0)

