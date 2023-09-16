import requests
import os
import json


def send_to_telegram(message):

    apiToken = os.getenv('BOT_KEY')
    chatID = '47651571'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
cotacoes = cotacoes.json()
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]
headers = {'Authorization': 'Bearer ' +  os.getenv('API_KEY')}
r = requests.get("https://hodlhodl.com/api/v1/offers?[side]=buy&filters[currency_code]=BRL", headers = headers)
prices = []
data = json.loads(r.content)
for offer in data['offers']:
    if offer['trader']['trades_count'] > 0 and float(cotacao_bitcoin) <= float(offer['price']) :
        prices.append({"id" :offer['id'],
                      "price" :float(offer['price']),
                      "login" :offer['trader']['login'],
                      "rating":offer['trader']['rating']})
sum_prices = 0
for item in prices:
    sum_prices+=item['price']
    
avg = sum_prices/len(prices)
print(f"PREÇO BTC: {cotacao_bitcoin:,}")
print(prices)

res = int(cotacao_bitcoin) + 5000    
for item in prices:
    if item['price'] >= res:
        rating = float(item['rating']) * 5
        msg = f""" 📣 NOVA OFERTA BARATA NA HODLHODL 📣  
            👤 USUÁRIO: {item['login']}
            ⭐️ RATING: {str(rating)}
            🔍PREÇO BTC: R$ {cotacao_bitcoin}
            🛎 PREÇO DO VENDEDOR: R$ {item['price']:,}
            🔗 https://hodlhodl.com/offers/{item['id']:,}"""
        send_to_telegram(msg)
    #else:
    #    send_to_telegram(f"PREÇO BITCOIN AGORA: R$ {cotacao_bitcoin}")
    #    send_to_telegram(f"Nenhuma promo boa por hora, só tem isso: {prices}")



