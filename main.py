import requests
import json
from pprint import pprint

def get_by_name():
    #jungle example
    
    url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD,EUR&api_key=1807c4f60d9e13e37eb0e8be99d280395b3f68ac5c31cf98bee8cc3832d364a4"
    res = requests.get(url)
    json = res.json()

    for i in json:
        price_btce = json['RAW']['BTC']['EUR']['PRICE']
        change24hour_btce = json['RAW']['BTC']['EUR']['CHANGE24HOUR']
        changeday_btce = json['RAW']['BTC']['EUR']['CHANGEDAY']
        high24hour_btce = json['RAW']['BTC']['EUR']['HIGH24HOUR']
        highday_btce = json['RAW']['BTC']['EUR']['HIGHDAY'] 
        low24hour_btce = json['RAW']['BTC']['EUR']['LOW24HOUR'] 
        lowday_btce = json['RAW']['BTC']['EUR']['LOWDAY']
    print("Euro price for BTC:\nprice: {};\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
    .format(price_btce, round(change24hour_btce, 2), round(changeday_btce, 2), high24hour_btce, highday_btce, low24hour_btce, lowday_btce))
    
    for i in json:
        price = json['RAW']['BTC']['USD']['PRICE']
        change24hour = json['RAW']['BTC']['USD']['CHANGE24HOUR']
        changeday = json['RAW']['BTC']['USD']['CHANGEDAY']
        high24hour = json['RAW']['BTC']['USD']['HIGH24HOUR']
        highday = json['RAW']['BTC']['USD']['HIGHDAY'] 
        low24hour = json['RAW']['BTC']['USD']['LOW24HOUR'] 
        lowday = json['RAW']['BTC']['USD']['LOWDAY']
    print("\nUSD price for BTC:\nprice: {};\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
    .format(price, round(change24hour, 2), round(changeday, 2), high24hour, highday, low24hour, lowday))

    for i in json:
        price = json['RAW']['ETH']['EUR']['PRICE']
        change24hour = json['RAW']['ETH']['EUR']['CHANGE24HOUR']
        changeday = json['RAW']['ETH']['EUR']['CHANGEDAY']
        high24hour = json['RAW']['ETH']['EUR']['HIGH24HOUR']
        highday = json['RAW']['ETH']['EUR']['HIGHDAY'] 
        low24hour = json['RAW']['ETH']['EUR']['LOW24HOUR'] 
        lowday = json['RAW']['ETH']['EUR']['LOWDAY']
    print("\nEuro price for ETH:\nprice: {};\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
    .format(price, round(change24hour, 2), round(changeday, 2), high24hour, highday, low24hour, lowday))

    for i in json:
        price = json['RAW']['ETH']['USD']['PRICE']
        change24hour = json['RAW']['ETH']['USD']['CHANGE24HOUR']
        changeday = json['RAW']['ETH']['USD']['CHANGEDAY']
        high24hour = json['RAW']['ETH']['USD']['HIGH24HOUR']
        highday = json['RAW']['ETH']['USD']['HIGHDAY'] 
        low24hour = json['RAW']['ETH']['USD']['LOW24HOUR'] 
        lowday = json['RAW']['ETH']['USD']['LOWDAY']
    print("\nUSD price for ETH:\nprice: {};\nchange24hour: {}\nchangeday: {}\nhigh24hour: {}\nhighday: {}\nlow24hour: {}\nlowday: {}"
    .format(price, round(change24hour, 2), round(changeday, 2), high24hour, highday, low24hour, lowday))

get_by_name()