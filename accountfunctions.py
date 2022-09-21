import time
import requests
import requests
import urllib.parse
import hashlib
import hmac
import base64

#Regular
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

def get_recent_withdrawals( api_key, api_sec):
    #take in input for asset
    asset = input("Enter the asset you want to see recent orders for: ")
    resp = kraken_request('/0/private/WithdrawStatus', {
    "nonce": str(int(1000*time.time())),
    "asset": asset
    }, api_key, api_sec)
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')

def get_withdrawal_info(api_key, api_sec):
    #take in input for asset
    asset = input("Enter the asset you want to see recent orders for: ")
    resp = kraken_request('/0/private/WithdrawStatus', {
    "nonce": str(int(1000*time.time())),
    "asset": asset
    }, api_key, api_sec)
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')
        
def withdraw_funds(api_key, api_sec):
    #take in input for asset
    asset = input("Enter the asset you want to withdraw: ")
    amount = input("Enter the amount you want to withdraw: ")
    resp = kraken_request('/0/private/Withdraw', {
    "nonce": str(int(1000*time.time())),
    "asset": asset,
    "amount": amount,
    }, api_key, api_sec)
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')

def request_withdrawal_cancelation( api_key, api_sec):
    #take in input for asset
    asset = input("Enter the asset you want for the withdrawal you want to cancel: ")
    refid = input("Enter the reference id of the withdrawal you want to cancel: ")
    resp = kraken_request('/0/private/WithdrawCancel', {
    "nonce": str(int(1000*time.time())),
    "asset": asset,
    "refid": refid
    }, api_key, api_sec)

    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')

def request_wallet_transfer( api_key, api_sec):
    #take in asset and ammount
    asset = input("Enter the asset you want to transfer: ")
    amount = input("Enter the amount you want to transfer: ")
    resp = kraken_request('/0/private/WalletTransfer', {
    "nonce": str(int(1000*time.time())),
    "asset": asset,
    "amount": amount
    }, api_key, api_sec)
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')


# def get_deposit_methods(api_key, api_sec):
#     resp = kraken_request('/0/private/DepositMethods', {
#          "nonce": str(int(1000*time.time())),
#          "asset": "XBT"},
#          api_key, api_sec)    
#           print(resp.json())
          
def get_deposit_address(api_key, api_sec):
    data = '/0/private/DepositAddresses', {
    "nonce": str(int(1000*time.time())),
    "asset": "XBT",
    "method": "Bitcoin",
    "new": True
    }

    resp = kraken_request(data, api_key, api_sec)
    if not resp.json()['error']:
        print(resp.json())
    else:
        print(f'Error: {resp.json()["error"]}')
