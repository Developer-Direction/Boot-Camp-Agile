# create a command line interface for the bot that runs and says "wwelcome to your Python Trading Bot"
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import order 
from tqdm.auto import tqdm
import Kraken_Request as kr




# print string to comand line welcome to your Python Trading Bot
print("Welcome to your Python Trading Bot")

# Prompt user to input API Key and API Secret upon initializing
# the bot and storing them in variables.
api_key = input("Please enter your API Key: ")
api_secret = input("Please enter your API Secret: ")

# run loop for bot
run = True


while run:

    # print on a new line chose what action you want to take
    # list of actions our users will take feel free to change names
    # make sure checks for valid input are in lower case
    print("Choose what action you want to take\n")
    print("Get Account Balance\n")
    print("Get Trades History\n")
    print("Add Order\n")
    print("Get Open Orders\n")
    print("Cancel Order\n")
    print("Get Order Book\n")
    print("Fund Account\n")
    print("Change Account\n")
    print("Exit\n")

    # get user input for action
    action = input("Enter action: ")

    # note to developers make sure checks for valid input are in lower case
    # convert action to lower case
    action = action.lower()

    # if user input is get account balance
    if action == "get account balance":
        # get account balance
        # get_account_balance()
        print("Account Balance is:")
        # sleep for 1 second to allow user to read output
        time.sleep(1)


    #if user input is get trades history
    if action == "get trades history":
        #request trades history
        resp = kr('/0/private/TradesHistory', {
            "nonce": str(int(1000*time.time())),
            # "type": <string> (default):"all" "any position" "closed position" "closing position" "no position"
            "trades": True
            # "start": <integer> Starting unix timestamp or trade tx ID of results (exclusive)
            # "end": <integer> Ending unix timestamp or trade tx ID of results (inclusive)
            # "ofs": <integer> Result offset for pagination
        }, api_key, api_secret)
        #print response
        if not resp.json()['error']:
            print(resp.json())
        else:
            print(f'Error: {resp.json()["error"]}')


    #if user input is get open orders
    if action == "get open orders":
        #request open orders
        resp = kr('/0/private/OpenOrders', {
            "nonce": str(int(1000*time.time())),
            "trades": True,
            # "userref": <integer> Restrict results to given user reference id
        }, api_key, api_secret)
        #print response
        if not resp.json()['error']:
            print(resp.json())
        else:
            print(f'Error: {resp.json()["error"]}')


    #if user input is cancel order
    if action == "cancel order":
        #input transaction id
        txid = input("Enter transaction id: ")
        #request cancel order
        resp = kr('/0/private/CancelOrder', {
            "nonce": str(int(1000*time.time())),
            "txid": txid
        }, api_key, api_secret)
        #print response
        if not resp.json()['error']:
            print(f'Order {txid} canceled...')
        else:
            print(f'Error: {resp.json()["error"]}')


    #if user input is get order book
    if action == "get order book":
        #input asset and count
        pair = input("Enter the asset pair you want to see: ")
        count = input(f'Enter the amount of asks/bids you want to see for {pair} (1-500): ')
        # request order book
        resp = requests.get('https://api.kraken.com/0/public/Depth', {
            "pair": pair,
            "count": count
        })
        #print response
        if not resp.json()['error']:
            print(resp.json())
        else:
            print(f'Error: {resp.json()["error"]}')    


    #if user input is change account, they'll be able to input a new
    #API Key and API Secret.
    if action == "change account":
        api_key = input("Please enter your API Key: ")
        api_secret = input("Please enter your API Secret: ")


    #if user input is add order, they'll be able to add an order
    if action == "add order":
        order.add_order()


    #if user action is exit then exit loop
    if action == "exit":
        run = False
        # if user action is not listed then print error message

    # consider rewriting to check from a listy instead of if else and a ton of conditionals
    elif action != "get account balance" and action != "get account history" and action != "get open orders" and action != "cancel order" and action != "fund account" and action != "change account":
        print("Error: Action not found")

    # print out equals line to denote comand complete
    print("\n"+"=" * 100+"\n")
    # sleep for 1 second to allow user to read output
    time.sleep(1)

    s = range(100)
    t = tqdm(total=len(s))
    for x in s:
        time.sleep(0.01)
        t.update()
        t.refresh()  # force print final state

    t.reset()  # reuse bar
    for x in s:
        t.update()
    t.close()  # close the bar permanently


# run loop end
print("Thank you for using our Python Trading Bot")
print("Have a nice day!")
# end of program
