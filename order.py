import time
import os 
import requests
from dotenv import load_dotenv
import Kraken_Request 

load_dotenv()

api_url = "https://api.kraken.com"

# I used my personal API keys to test but will probably need to change this if we are
#requring the user to enter API key and API Secret.
api_key = os.getenv('API_KEY')
api_sec = os.getenv('API_SECRET')

#stores the user input (variables) as a global object
kracken_data = {
  "nonce": str(int(1000*time.time())),
  "ordertype": "",
  "type": "",
  "volume": "",
  "pair": "",
  "price": "",
}

# User will be asked to enter the specific price and after entering it, 
#user will be asked if ready to place the order. Need to come up with more 
#conditions?
def price():
  price = input("Please enter the specific price\n")
  if price:
    print("Are you ready to submit your order?\n")
    print("1.)YES")
    print("2.)NO")

    answer = input()
    if answer == "1":
        kracken_data["price"] = price
        place_order()
    elif answer == "2":
        price()
    else:
        print("Wrong input")
        price()


# User will be asked to enter the specific volume. Might need to come up with more 
#conditions?
def volume():
  volume = input("Please enter the specific volume of base currency\n")
  if volume:
    kracken_data["volume"] = volume
    price()
  else:
    print("Wrong input")
    volume()


# User will be asked to enter the type of transaction. Might need to come up with more 
#conditions?
def type_trans():
  typeTrans = input("Please enter the type of transaction\n")
  if typeTrans:
    kracken_data["type"] = typeTrans
    volume()
  else:
    print("Wrong input")
    type_trans()


# User will be asked to enter the specific order type. Might need to come up with more 
#conditions?
def order_type():
  orderType = input("Please enter your desired order type\n")
  if orderType:
    kracken_data["ordertype"] = orderType
    type_trans()
  else:
    print("Wrong input")
    order_type()


# User will be asked to enter the specific trading pair. Might need to come up with more 
#conditions?
def add_order():
  pair = input("Please enter the trading pair\n")
  if pair:
    kracken_data["pair"] = pair
    # setattr(kracken_data, "pair", pair)
    order_type()
  else:
    print("Wrong input")
    add_order()


#Place order function is called after the user enters the price. This function does
#the API call.
def place_order():
  def kraken_request(url_path, data, api_key, api_sec):
    headers={}
    headers['API-key'] = api_key
    headers['API-Sign'] = Kraken_Request.get_kraken_signature(url_path, data, api_sec)
    req = requests.post((api_url + url_path), headers=headers, data=data)
    return req
  
  try:
    resp = kraken_request('/0/private/AddOrder', kracken_data, api_key, api_sec)
    print(resp.json())
  
  except resp.exceptions.HTTPError as err:
    return  repr(err)
    print("Error")
    
  

