import requests
import telebot
from telebot import types

#bot token
bot = telebot.TeleBot('Your_Tgbot_Token')
    
#start function
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.InlineKeyboardButton("Crypto")
    markup.add(btn1)
    bot.reply_to(message, "Hello, want to know more about cryptocurrency, click the button Crypto and become knowledgeable", reply_markup=markup)

    #request button
    @bot.message_handler(regexp="Crypto")
    def send_welcome(message):
        msg = bot.send_message(message.chat.id, text="Type crypto in format (BTC)")
        bot.register_next_step_handler(msg, define)

    #main function
    def define(message):
        message_text = str(message.text).upper()
        #api connection
        url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,EUR&api_key=Your_Api_key".format(message_text)
        res = requests.get(url)
        json = res.json()
        try:
            if json['Response'] == "Error":
                bot.send_message(message.chat.id, text=f"Sorry crypto {message_text} wasn't found, please try other one. Or you can stop searching with command stop")
                send_welcome(message)
        except Exception:
            if message.text == "stop":
                bot.send_message(message.chat.id, text="You stop searching. If you want to cintinue click the button /Crypto")
                quit()
            for i in json:
                price_euro = json['RAW'][f'{message_text}']['EUR']['PRICE']
                change24hour_euro = json['RAW'][f'{message_text}']['EUR']['CHANGE24HOUR']
                changeday_euro = json['RAW'][f'{message_text}']['EUR']['CHANGEDAY']
                high24hour_euro = json['RAW'][f'{message_text}']['EUR']['HIGH24HOUR']
                highday_euro = json['RAW'][f'{message_text}']['EUR']['HIGHDAY'] 
                low24hour_euro = json['RAW'][f'{message_text}']['EUR']['LOW24HOUR'] 
                lowday_euro = json['RAW'][f'{message_text}']['EUR']['LOWDAY']
            bot.send_message(message.chat.id, text="Euro price for {}:\nprice: {}\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
            .format(message_text, price_euro, round(change24hour_euro, 2), round(changeday_euro, 2), high24hour_euro, highday_euro, low24hour_euro, lowday_euro))
            for i in json:
                price_usd = json['RAW'][f'{message_text}']['USD']['PRICE']
                change24hour_usd = json['RAW'][f'{message_text}']['USD']['CHANGE24HOUR']
                changeday_usd = json['RAW'][f'{message_text}']['USD']['CHANGEDAY']
                high24hour_usd = json['RAW'][f'{message_text}']['USD']['HIGH24HOUR']
                highday_usd = json['RAW'][f'{message_text}']['USD']['HIGHDAY'] 
                low24hour_usd = json['RAW'][f'{message_text}']['USD']['LOW24HOUR'] 
                lowday_usd = json['RAW'][f'{message_text}']['USD']['LOWDAY']
            bot.send_message(message.chat.id, text="USD price for {}:\nprice: {}\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
            .format(message_text, price_usd, round(change24hour_usd, 2), round(changeday_usd, 2), high24hour_usd, highday_usd, low24hour_usd, lowday_usd))
            if change24hour_euro > 1000:
                bot.send_message(message.chat.id, text="Currently, the price of this cryptocurrency is growing rapidly, a good opportunity to buy")
            elif change24hour_euro <= 0:
                bot.send_message(message.chat.id, text="Currently, the price of this cryptocurrency is falling, it is not the best option to buy, look for something else")
            else:
                bot.send_message(message.chat.id, text="Currently, the price of this cryptocurrency is growing slowly. You can buy at your own risk")
            bot.send_message(message.chat.id, text="You can always stop searching with command stop")
            send_welcome(message)

bot.infinity_polling()

