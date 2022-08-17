import time
import requests
import requests
import urllib.parse
import hashlib
import hmac
import base64





api_url = 'https://api.kraken.com'

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


def trades_history(api_key, api_sec):
    resp = kraken_request('/0/private/TradesHistory', {
        "nonce": str(int(1000*time.time())),
        # "type": <string> (default):"all" "any position" "closed position" "closing position" "no position"
        "trades": True
        # "start": <integer> Starting unix timestamp or trade tx ID of results (exclusive)
        # "end": <integer> Ending unix timestamp or trade tx ID of results (inclusive)
        # "ofs": <integer> Result offset for pagination
    }, api_key, api_sec)

    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')


def open_orders(api_key, api_sec):
    resp = kraken_request('/0/private/OpenOrders', {
        "nonce": str(int(1000*time.time())),
        "trades": True,
        # "userref": <integer> Restrict results to given user reference id
    }, api_key, api_sec)

    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')


def cancel_order(api_key, api_sec):
    #input transaction id
    txid = input("Enter transaction id: ")
    resp = kraken_request('/0/private/CancelOrder', {
        "nonce": str(int(1000*time.time())),
        "txid": txid
    }, api_key, api_sec)

    if not resp.json()['error']:
        print(f'Order {txid} canceled...')
    else:
        print(f'Error: {resp.json()["error"]}')


def get_order_book():
    #input asset and count
    pair = input("Enter the asset pair you want to see: ")
    count = input(f'Enter the amount of asks/bids you want to see for {pair} (1-500): ')
    resp = requests.get('https://api.kraken.com/0/public/Depth', {
        "pair": pair,
        "count": count
    })
   
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')  