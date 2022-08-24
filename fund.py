# create a command line interface for the bot that runs and says "wwelcome to your Python Trading Bot"
from pyclbr import Function
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import Kraken_Request as kr

#print string to comand line welcome to your Python Trading Bot
print("Welcome to your Python Trading Bot")

#Prompt user to input API Key and API Secret upon initializing
#the bot and storing them in variables.
api_key = input("Please enter your API Key: ")
api_secret = input("Please enter your API Secret: ")

#run loop for bot
run = True
while run:
    
    #print on a new line chose what action you want to take
    #list of actions our users will take feel free to change names
    #make sure checks for valid input are in lower case
    print("Choose what action you want to take\n")
    print("Get Account Balance\n")
    print("Get Account History\n")
    print("Get Open Orders\n")
    print("Cancel Order\n")
    print("Fund Menu\n")
    print("Fund Account\n")
    print("Change Account\n")
    print("Exit\n")
    
    #get user input for action
    action = input("Enter action: ")
    #note to developers make sure checks for valid input are in lower case
    #convert action to lower case
    action = action.lower()

    #Fund Menu option
    def fund_menu():
        print("[1] Fund Method")
        print("[2] Funding Address")
        print("exit")

        fund_menu()

        fundOption = int(input("Enter your method: "))

        # Options for fund mennu
        while fundOption != 0:
            if fundOption == 1:
                print("Method has been called.")
    
            if fundOption != 0:
                print("Enter your address: ")
    
            else: 
                print("Invalid address")

        print()
        fund_menu()

        fundOption = int(input("Enter your address: "))

    
    # Fund account
    action = input("Fund Account: ")

    #if user input is fund account
    if action == "Fund Account":
        fund_Account()

    # function for funding account address and funding method
    def fund_Account():
        data = '/0/private/DepositAddresses', {
        "nonce": str(int(1000*time.time())),
        "asset": "XBT",
        "method": "Bitcoin",
        "new": True
        }, api_key, api_secret

        data = '/0/private/DepositMethods', {
        "nonce": str(int(1000*time.time())),
        "asset": "XBT"
        }, api_key, api_sec

        # kraken request
        kraken_request()

     #if user input is get account balance
    if action == "get account balance":
        #get account balance
        #get_account_balance()
        print("Account Balance is:")
        #sleep for 1 second to allow user to read output
        time.sleep(1)
        
    #if user input is change account, they'll be able to input a new
    #API Key and API Secret.
    if action == "change account":
        api_key = input("Please enter your API Key: ")
        api_secret = input("Please enter your API Secret: ")

    
    
    #if user action is exit then exit loop
    if action == "exit":
        run = False
        #if user action is not listed then print error message
    
    #consider rewriting to check from a listy instead of if else and a ton of conditionals
    elif action != "get account balance" and action != "get account history" and action != "get open orders" and action != "cancel order" and action != "fund account" and action != "change account":
        print("Error: Action not found")
    
    
    #print out equals line to denote comand complete
    print("\n"+"=" * 100+"\n")
    #sleep for 1 second to allow user to read output
    time.sleep(1)

#run loop end
print ("Thank you for using our Python Trading Bot")
print ("Have a nice day!")
#end of program
