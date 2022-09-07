import time
import requests
import requests
import urllib.parse
import hashlib
import hmac
import base64
import Kraken_Request as kr

# load_dotenv()

api_url = "https://api.kraken.com"

def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def kraken_request(url_path, data, api_key, api_sec):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature(url_path, data, api_sec)}
    response = requests.post((api_url + url_path), headers=headers, data=data)
    return response


def add_order(api_key, api_sec):
    #input the type of order, transaction, currency pair, volume, and price
    ordertype = input("Enter the type of order you'd like to place: ")
    transaction = input("Enter the type of transaction: ")
    volume = input("Enter the type of volume: ")
    pair = input("Enter the trading pair: ")
    price = input("Enter the price: ")
    resp = kraken_request('/0/private/AddOrder', {
    "nonce": str(int(1000*time.time())),
    "ordertype": ordertype,
    "type": transaction,
    "volume": volume,
    "pair": pair,
    "price": price
    }, api_key, api_sec)
    if not resp.json()['error']:
      print(resp.json())
    else:
      print(f'Error: {resp.json()["error"]}')
    

  

