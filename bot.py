# create a command line interface for the bot that runs and says "wwelcome to your Python Trading Bot"
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

#variables
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

#print string to comand line welcome to your Python Trading Bot
print("Welcome to your Python Trading Bot")
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
    print("Fund Account\n")
    print("Exit\n")
    
    #get user input for action
    action = input("Enter action: ")
    #note to developers make sure checks for valid input are in lower case
    #convert action to lower case
    action = action.lower()

    #if user input is get account balance
    if action == "get account balance":
        #get account balance
        #get_account_balance()
        print("Account Balance is:")
        #sleep for 1 second to allow user to read output
        time.sleep(1)
    
    #if user action is exit then exit loop
    if action == "exit":
        run = False
        #if user action is not listed then print error message
    
    #consider rewriting to check from a listy instead of if else and a ton of conditionals
    elif action != "get account balance" and action != "get account history" and action != "get open orders" and action != "cancel order" and action != "fund account":
        print("Error: Action not found")
    
    
    #print out equals line to denote comand complete
    print("\n"+"=" * 100+"\n")
    #sleep for 1 second to allow user to read output
    time.sleep(1)

#run loop end
print ("Thank you for using our Python Trading Bot")
print ("Have a nice day!")
#end of program