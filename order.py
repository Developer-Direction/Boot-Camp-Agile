import time
import os 
import requests
from dotenv import load_dotenv

load_dotenv()

api_url = "https://api.kraken.com"
api_key = os.environ.get(API_KEY)
api_secret = os.environ.get(API_SECRET)


def add_order 
payload = {
  "event": "addOrder",
  "ordertype": "limit",
  "pair": "XBT/USD",
  "price": "9000",
  "token": "0000000000000000000000000000000000000000",
  "type": "buy",
  "volume": "10.123"
}
