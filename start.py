from lib.db_manager import db_manager
from lib.db_coron import db_coron
from lib.settings import *
from telebot import types
import telebot
import random


__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, __URL, token)
covid_19_data = db_object.get_all_data()
db_object.save_all_data(covid_19_data)
coron_db = db_coron()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def keyboard(message):
    sti = open('image/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("☠️ COVID 19 ☠️")
    item2 = types.KeyboardButton("☠️ UPDATE COVID 19 ☠️")
    key.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы облегчить вам жизнь.".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=key)


@bot.message_handler(content_types=['text'])
def Klava(message):
    if message.chat.type == 'private':
        if message.text == '☠️ UPDATE COVID 19 ☠️':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '☠️ COVID 19 ☠️':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(
                "🌏 Дані всіх країн 🌏", callback_data='global')
            item2 = types.InlineKeyboardButton(
                "🌏 Дані однієї країни 🌏", callback_data='one')

            markup.add(item1, item2)

            bot.send_message(
                message.chat.id, '\t🙏 Вибери Щось 🙏', reply_markup=markup)
        vyb_Country = 0
        con = "0"
        coc = "0"
        coron_db.zap(covid_19_data)
        cor = coron_db.vyvid(vyb_Country, con, coc)
        for item in cor:
            if message.text == item[1]:
                bot.send_message(message.chat.id, "=================================\n"+"\n⬇️💩Країна💩⬇️ \n     " + str(item[1]) + "\n⬇️🥵Кількість захворюваннь за добу🥵⬇️ \n     " + str(
                    item[4]) + "\n⬇️🥵Кількість захворюваннь🥵⬇️ \n     " + str(item[5]) + "\n⬇️☠️Кількість смертей за добу☠️⬇️\n     " + str(item[6]) + "\n⬇️☠️Кількість смертей☠️⬇️\n      " + str(item[7]) + "\n⬇️💊Кількість вилікуваних за добу💊⬇️\n     " + str(item[8]) + "\n⬇️💊Кількість вилікуваних💊⬇️\n     " + str(item[9]) + "\n=================================\n")
            elif message.text == item[2]:
                bot.send_message(message.chat.id, "=================================\n"+"\n⬇️💩Країна💩⬇️ \n     " + str(item[1]) + "\n⬇️🥵Кількість захворюваннь за добу🥵⬇️ \n     " + str(
                    item[4]) + "\n⬇️🥵Кількість захворюваннь🥵⬇️ \n     " + str(item[5]) + "\n⬇️☠️Кількість смертей за добу☠️⬇️\n     " + str(item[6]) + "\n⬇️☠️Кількість смертей☠️⬇️\n      " + str(item[7]) + "\n⬇️💊Кількість вилікуваних за добу💊⬇️\n     " + str(item[8]) + "\n⬇️💊Кількість вилікуваних💊⬇️\n     " + str(item[9]) + "\n=================================\n")

        else:
            bot.send_message(message.chat.id, 'ОК 😢')


# @bot.message_handler(content_types=['text'])
# def krain(message):
#     vyb_Country = 0
#     con = "0"
#     coc = "0"
#     coron_db.zap(covid_19_data)
#     cor = coron_db.vyvid(vyb_Country, con, coc)
#     for item in cor:
#         if message.text == item[1]:
#             bot.send_message(message.chat.id, "=================================\n"+"\n⬇️💩Країна💩⬇️ \n     " + str(item[1]) + "\n⬇️🥵Кількість захворюваннь за добу🥵⬇️ \n     " + str(
#                 item[4]) + "\n⬇️🥵Кількість захворюваннь🥵⬇️ \n     " + str(item[5]) + "\n⬇️☠️Кількість смертей за добу☠️⬇️\n     " + str(item[6]) + "\n⬇️☠️Кількість смертей☠️⬇️\n      " + str(item[7]) + "\n⬇️💊Кількість вилікуваних за добу💊⬇️\n     " + str(item[8]) + "\n⬇️💊Кількість вилікуваних💊⬇️\n     " + str(item[9]) + "\n=================================\n")
#         elif message.text == item[2]:
#             bot.send_message(message.chat.id, "=================================\n"+"\n⬇️💩Країна💩⬇️ \n     " + str(item[1]) + "\n⬇️🥵Кількість захворюваннь за добу🥵⬇️ \n     " + str(
#                 item[4]) + "\n⬇️🥵Кількість захворюваннь🥵⬇️ \n     " + str(item[5]) + "\n⬇️☠️Кількість смертей за добу☠️⬇️\n     " + str(item[6]) + "\n⬇️☠️Кількість смертей☠️⬇️\n      " + str(item[7]) + "\n⬇️💊Кількість вилікуваних за добу💊⬇️\n     " + str(item[8]) + "\n⬇️💊Кількість вилікуваних💊⬇️\n     " + str(item[9]) + "\n=================================\n")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'global':
                vyb_Country = 0
                con = "0"
                coc = "0"
                coron_db.zap(covid_19_data)
                cor = coron_db.vyvid(vyb_Country, con, coc)
                for item in cor:
                    bot.send_message(call.message.chat.id, "=================================\n"+"\n⬇️💩Країна💩⬇️ \n     " + str(item[1]) + "\n⬇️🥵Кількість захворюваннь за добу🥵⬇️ \n     " + str(
                        item[4]) + "\n⬇️🥵Кількість захворюваннь🥵⬇️ \n     " + str(item[5]) + "\n⬇️☠️Кількість смертей за добу☠️⬇️\n     " + str(item[6]) + "\n⬇️☠️Кількість смертей☠️⬇️\n      " + str(item[7]) + "\n⬇️💊Кількість вилікуваних за добу💊⬇️\n     " + str(item[8]) + "\n⬇️💊Кількість вилікуваних💊⬇️\n     " + str(item[9]) + "\n=================================\n")

            elif call.data == 'one':
                bot.send_message(call.message.chat.id,
                                 "Введіть країну!!!")

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Дані відправлено!",
                                  reply_markup=None)

            # # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #                           text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
# @bot.message_handler(content_types=["text"])
# def main(message):
#     # countr = message.text
#     # countr_cod = message.text
#     # vyb_corona = db_object.show_country(countr)
#     # vyb_corona_cod = db_object.show_country_CountryCode(countr_cod)
#     if message.text == "COVID 19":
#         keyboard2(message)
#         # bot.send_message(message.chat.id, "Вы нажали 1")

#     elif message.text == "Countries":
#         keyboard3(message)
#         bot.send_message(message.chat.id, "Вы нажали 2")
#     elif message.text == "Country Name":
#         bot.send_message(message.chat.id, "Enter Country Name")

#     elif message.text == "Country Code":
#         bot.send_message(message.chat.id, "Enter Country Code")

#     elif message.text == "UPDATE COVID 19":
#         print("test")

#     elif message.text == "All countrie":
#         vyb_Country = 0
#         con = "0"
#         coc = "0"
#         coron_db.zap(covid_19_data)
#         cor = coron_db.vyvid(vyb_Country, con, coc)
#         for item in cor:
#             bot.send_message(message.chat.id, "=================================\n"+"\nCountry => \t\t" + str(item[1]) + "\nCountryCode => \t\t" + str(item[2]) + "\nSlug => \t\t" + str(item[3]) + "\nNewConfirmed => \t" + str(
#                 item[4]) + "\nTotalConfirmed => \t" + str(item[5]) + "\nNewDeaths => \t\t" + str(item[6]) + "\nTotalDeaths => \t\t" + str(item[7]) + "\nNewRecovered => \t" + str(item[8]) + "\nTotalRecovered => \t" + str(item[9]) + "\n=================================\n")
#     else:
#         main1(message)
#     # elif message.text == countr:
#     #     for item in vyb_corona:
#     #         bot.send_message(message.chat.id, "=================================\n"+"\nCountry => \t\t" + str(item[1]) + "\nCountryCode => \t\t" + str(item[2]) + "\nSlug => \t\t" + str(item[3]) + "\nNewConfirmed => \t" + str(
#     #             item[4]) + "\nTotalConfirmed => \t" + str(item[5]) + "\nNewDeaths => \t\t" + str(item[6]) + "\nTotalDeaths => \t\t" + str(item[7]) + "\nNewRecovered => \t" + str(item[8]) + "\nTotalRecovered => \t" + str(item[9]) + "\n=================================\n")

#     # elif message.text == countr:
#     #     for item in vyb_corona_cod:
#     #         bot.send_message(message.chat.id, "=================================\n"+"\nCountry => \t\t" + str(item[1]) + "\nCountryCode => \t\t" + str(item[2]) + "\nSlug => \t\t" + str(item[3]) + "\nNewConfirmed => \t" + str(
#     #             item[4]) + "\nTotalConfirmed => \t" + str(item[5]) + "\nNewDeaths => \t\t" + str(item[6]) + "\nTotalDeaths => \t\t" + str(item[7]) + "\nNewRecovered => \t" + str(item[8]) + "\nTotalRecovered => \t" + str(item[9]) + "\n=================================\n")


# @bot.message_handler(commands=["st"])
# def keyboard2(message):
#     key = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key.row('Countries', 'All countrie')
#     bot.send_message(message.chat.id, "Enter comand", reply_markup=key)


# @bot.message_handler(commands=["s"])
# def keyboard3(message):
#     key = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     key.row('Country Name', 'Country Code')
#     bot.send_message(message.chat.id, "Enter comand", reply_markup=key)


# @bot.message_handler(content_types=["text"])
# def main1(message):
#     countr = message.text
#     countr_cod = message.text
#     #vyb_corona = db_object.show_country(countr)
#     vyb_corona_cod = db_object.show_country_CountryCode(countr_cod)
#     # if message.text == countr:
#     #     for item in vyb_corona:
#     #         bot.send_message(message.from_user.id, "=================================\n"+"\nCountry => \t\t" + (item[1]) + "\nCountryCode => \t\t" + (item[2]) + "\nSlug => \t\t" + (item[3]) + "\nNewConfirmed => \t" + (
#     #             item[4]) + "\nTotalConfirmed => \t" + (item[5]) + "\nNewDeaths => \t\t" + (item[6]) + "\nTotalDeaths => \t\t" + (item[7]) + "\nNewRecovered => \t" + (item[8]) + "\nTotalRecovered => \t" + (item[9]) + "\n=================================\n")

#     if message.text == countr:
#         for item in vyb_corona_cod:
#             bot.send_message(message.chat.id, "=================================\n"+"\nCountry => " + str(item[1]) + "\nCountryCode => " + str(item[2]) + "\nSlug => " + str(item[3]) + "\nNewConfirmed => \t" + int(
#                 item[4]) + "\nTotalConfirmed => " + int(item[5]) + "\nNewDeaths => " + int(item[6]) + "\nTotalDeaths => " + int(item[7]) + "\nNewRecovered => " + int(item[8]) + "\nTotalRecovered => " + int(item[9]) + "\n=================================\n")


# if __name__ == "__main__":
#     bot.polling(none_stop=True)


# def menyu(covid_19_data):
#     exit = True
#     while exit:
#         vyb = int(
#             input("1. Вивести дані COVID 19 \t2. Обновити дані COVID 19\t0. EXIT => "))
#         if vyb == 1:
#             vyb2 = int(input("1.Вивести дані \"КРАЇНИ\"\t2. All countries => "))
#             vyb_Country = 0
#             con = "0"
#             coc = "0"
#             if vyb2 == 1:
#                 vyb_Country = int(
#                     input("1. Country Name\t2. Country Code => "))
#                 if vyb_Country == 1:
#                     con = input("Country Name => ")
#                     coron_db.zap(covid_19_data)
#                     coron_db.vyvid(vyb_Country, con, coc)
#                 elif vyb_Country == 2:
#                     coc = input("Country Code => ")
#                     coron_db.zap(covid_19_data)
#                     coron_db.vyvid(vyb_Country, con, coc)
#             elif vyb2 == 2:
#                 coron_db.zap(covid_19_data)
#                 coron_db.vyvid(vyb_Country, con, coc)
#         elif vyb == 2:
#             coron_db.zap(covid_19_data)
#             print("Update coron GOOD")
#         elif vyb == 0:
#             exit = False


# # menyu(covid_19_data)
