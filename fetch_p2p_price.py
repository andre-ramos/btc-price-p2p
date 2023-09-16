import requests
import os
import json


def send_to_telegram(message):

    apiToken = os.getenv('BOT_KEY')
    chatID = '47651571'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    print(apiURL)

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
cotacoes = cotacoes.json()
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]
print("Aqui"+ os.getenv('API_KEY'))
headers = {'Authorization': 'Bearer ' +  os.getenv('API_KEY')}
r = requests.get("https://hodlhodl.com/api/v1/offers?[side]=buy&filters[currency_code]=BRL", headers = headers)
prices = []
data = json.loads(r.content)
for offer in data['offers']:
    if offer['trader']['trades_count'] > 0 and float(cotacao_bitcoin) <= float(offer['price']) :
        prices.append(float(offer['price']))
avg = sum(prices)/len(prices)
print(f"PREÇO BTC: {cotacao_bitcoin}")
print(prices)

for price in prices:
    res = int(cotacao_bitcoin) + 5000    
    if price >= res:
        rating = float(offer['trader']['rating']) * 5
        msg = f""" 📣 NOVA OFERTA BARATA NA HODLHODL 📣  
            👤 USUÁRIO: {offer['trader']['login']}
            ⭐️ RATING: {str(rating)}
            _PREÇO BTC: R$ {cotacao_bitcoin},
            _PREÇO DO VENDEDOR: {price}
            🔗 https://hodlhodl.com/offers/{offer['id']}"""
        send_to_telegram(msg)
    #else:
    #    send_to_telegram(f"PREÇO BITCOIN AGORA: R$ {cotacao_bitcoin}")
    #    send_to_telegram(f"Nenhuma promo boa por hora, só tem isso: {prices}")



