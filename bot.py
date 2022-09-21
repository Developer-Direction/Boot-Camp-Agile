# create a command line interface for the bot that runs and says "wwelcome to your Python Trading Bot"
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64
import addorder 
import accountfunctions
from tqdm.auto import tqdm
import Kraken_Request as kr
import os

# print string to comand line welcome to your Python Trading Bot
print("Welcome to your Python Trading Bot!")

# Prompt user to input API Key and API Secret upon initializing
# the bot and storing them in variables.
api_key = input("Please enter your API Key: ")
api_secret = input("Please enter your API Secret: ")

# function for funding account address and funding method
# def fund_Account():
#     data = '/0/private/DepositAddresses', {
#     "nonce": str(int(1000*time.time())),
#     "asset": "XBT",
#     "method": "Bitcoin",
#     "new": True
#     }, api_key, api_secret
#     data = '/0/private/DepositMethods', {
#     "nonce": str(int(1000*time.time())),
#     "asset": "XBT"
#     }, api_key, api_secret
#     # kraken request
#     #print(Kraken_Request()) 
#     #make a call to Kraken_Request passing above info
#     #grab resulkt
#     #print result
#     kr.kraken_request()

# Fund Menu
# def fund_menu():
#     print("1. Fund Method")
#     print("2. Funding Address")
#     print("exit")
#     fund_menu()
#     fundOption = int(input("Enter your method: "))
#     # Options for fund mennu
#     while fundOption != 0:
#         if fundOption == 1:
#             print("Method has been called.")
#         if fundOption != 0:
#             print("Enter your address: ")
#         else: 
#             print("Invalid address")
#     print()
#     fund_menu()
#     fundOption = int(input("Enter your address: "))

def command_end():    
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

# run loop for bot
run = True

while run:

    # print on a new line chose what action you want to take
    # list of actions our users will take feel free to change names
    # make sure checks for valid input are in lower case
    print("What would you like to do?\n")
    print("1. Get Asset Info")
    print("2. Get Order Book")
    print("3. Get Trades History")
    print("4. Get Account Balance")
    print("5. Get Account History")
    print("6. Get Open Orders")
    print("7. Add Order")
    print("8. Cancel Order")
    print("9. Fund Account")
    print("10. Withdraw Funds")
    print("11. Request Withdrawal Cancellation")
    print("12. Get Recent withdrawals")
    print("13. Get Withdrawal Info")
    print("14. Request Wallet Transfer")
    print("15. Change Account")
    print("16. Get System Status")
    print("17. Exit\n")

    # get user input for action

    action = input("Enter the number of your desired option: ")

    match action:
        case "1":
            #if user input is get asset info
            # they will be able to search for all the assets or a specific pair
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
            command_end()
        
        case "2":
            #if user input is get order book
            accountfunctions.get_order_book()
            command_end()

        case "3":
            accountfunctions.trades_history(api_key, api_secret)
            command_end()

        case "4":
            # get account balance
            # get_account_balance()
            print("Account Balance is:")
            # sleep for 1 second to allow user to read output
            time.sleep(1)
            command_end()
        
        case "5":
            #if user input is get account history
            command_end()
        
        case "6":
            #if user input is get open orders
            accountfunctions.open_orders(api_key, api_secret)
            command_end()

        case "7":
            addorder.add_order(api_key, api_secret)
            command_end()
        
        case "8":
            #if user input is cancel order
            accountfunctions.cancel_order(api_key, api_secret)
            command_end()
        
        case "9":
            #if user input is fund account
            fund_Account()
            command_end()
        
        case "10":
            #if user action is withdraw funds
            accountfunctions.withdraw_funds(api_key, api_secret)
            time.sleep(1)
            command_end()
        
        case "11":
            #if user action is request withdrawal cancellation
            accountfunctions.request_withdrawal_cancellation(api_key, api_secret)
            time.sleep(1)
            command_end()
            
        case "12":
            #if user input is get status of recent withdrawals
            accountfunctions.get_recent_withdrawals(api_key, api_secret)
            time.sleep(1)
            command_end()
        
        case "13":
            #if user input is get withdrawal info
            accountfunctions.get_withdrawal_info(api_key, api_secret)
            time.sleep(1)
            command_end()
        
        case "14":
            #if user action is request wallet transfer
            accountfunctions.request_wallet_transfer(api_key, api_secret)
            time.sleep(1)
            command_end()
        
        case "15":
            #if user input is change account, they'll be able to input a new
            #API Key and API Secret.
            api_key = input("Please enter your API Key: ")
            api_secret = input("Please enter your API Secret: ")
            print("\nYou have changed accounts.")
            command_end()
        
        case "16":
            # get system status
            # get_system_status()
            resp = requests.get('https://api.kraken.com/0/public/SystemStatus')
            print("System Status is:")
            print(resp.json())
            # sleep for 1 second to allow user to read output
            time.sleep(1)
            command_end()

        case "17":
            #if user action is exit then exit loop
            run = False
            command_end()

        case _:
            #if user action is not listed then print error message 
            print("Error: Action not found")
            command_end()

# run loop end
print("Thank you for using our Python Trading Bot,")
print("Have a nice day!")
# end of program