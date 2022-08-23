# create a command line interface for the bot that runs and says "wwelcome to your Python Trading Bot"
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import order 
import accountfunctions
from tqdm.auto import tqdm
import Kraken_Request as kr
import os




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
    print("Get Account History\n")
    print("Get Open Orders\n")
    print("Cancel Order\n")
    print("Get asset info\n")
    print("Fund Account\n")
    print("Change Account\n")
    print("Get System Status\n")
    print("get recent withdrawls")
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

    #if user input is get status of recent withdrawals
    if action == "get recent withdrawls":
        accountfunctions.get_recent_withdrawls(api_key, api_secret)
        time.sleep(1)

    #if user input is get trades history
    if action == "get trades history":
        accountfunctions.trades_history(api_key, api_secret)


    #if user input is get open orders
    if action == "get open orders":
        accountfunctions.open_orders(api_key, api_secret)


    #if user input is cancel order
    if action == "cancel order":
        accountfunctions.cancel_order(api_key, api_secret)

    #if user input is get asset info
    # they will be able to search for all the assets or a specific pair
    if action == "get asset info":
        time.sleep(1)
        answer = input("You can either get all pairings using 'all', a specific pairing by name 'BTC/USD' or exit using 'cancel'\n")
        if answer == "all":
            ##get all pairings and display them
            resp = requests.get('https://api.kraken.com/0/public/Assets')
            print(resp.json())
            
        elif answer == "cancel":
            #get out of the if loop
            continue
        else: #get the ticker related to the input
            url_link = "https://api.kraken.com/0/public/Ticker?pair=" #partial URL to complete with the appropriate ticker
            complete_url = url_link + answer
            resp = requests.get(complete_url)
            print(resp.json())
        time.sleep(1)

    #if user input is get order book
    if action == "get order book":
        accountfunctions.get_order_book()

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

    
    if action == "get system status":
        # get system status
        # get_system_status()
        resp = requests.get('https://api.kraken.com/0/public/SystemStatus')
        print("System Status is:")
        print(resp.json())
        # sleep for 1 second to allow user to read output
        time.sleep(1)
    
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
