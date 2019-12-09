"""
This is Telegram bot getting a price and rating of FIFA player by the player's name from FUTBIN.com
"""

import telebot
import requests
from bs4 import BeautifulSoup
import re

token = "token_token"  #type your bot token or path to file with token

bot = telebot.TeleBot(token)  #from telebot (library) get method TeleBot

globalId = 0

@bot.message_handler(commands=['start'])  #launching the bot


def send_message (message):  #default function
    global chatId
    chatId = message.chat.id
    name = message.chat.first_name
    surname = message.chat.last_name
    username = message.chat.username
    bot.send_message(chat_id=chatId, text="Which player's price do you want to know, " + name + "?") #asking for player's name for forming request


@bot.message_handler(content_types=["text"])

def send_message(message):
    player = message.text
    url = "https://www.futbin.com/20/players?page=1&search="
    link = url + player
    data = requests.get(link).text      #forming request of player data from Futbin
    soup = BeautifulSoup(data, "lxml")      #getting player data 
    rate_range = soup.find_all("span", class_ = re.compile("form rating ut20"))     #getting player's rating
    list1 = []
    list2 = []
    for item in rate_range:
        rate = item.text
        list1.append(rate)
    price_range = soup.find_all("span", {"class": "ps4_color font-weight-bold"})   #getting player's price 
    for item in price_range:
        price = item.text
        list2.append(price)
    d = dict(zip(list1, list2))    #forming answer with player's rating & price 
    result = []
    for x in d:
        line = x + " -- " + d[x]
        result.append(line)
    ololo = str(" \n".join(result))
    bot.send_message(chat_id = chatId, text = ololo)    #sending info about requested player

bot.polling(none_stop = True)


