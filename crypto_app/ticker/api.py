import requests

def get_bitcoin_price():
    response = requests.get('https://blockchain.info/ticker')
    data = response.json()
    return data['USD']['last']

