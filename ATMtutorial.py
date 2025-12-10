import time # imports the time and random module
import random

money = random.randint(1,1000) # like the dice roller, creates a number from 1,1000 as your balance
print("Welcome to the ATM") 

choice = input("Would you like to 'withdraw' or see your 'balance'? ").lower()

if choice == "balance": # if you choose balance it does everthing in the if statement
    print("Your Balance is:")
    time.sleep(1.2)
    print(money)

elif choice == "withdraw": # if you choose withdraw it does everthing in the if statement
    withdraw_amount = int(input("How much would you like to withdraw? (10,20,30,40,50,60,70) "))

    if withdraw_amount in [10,20,30,40,50,60,70] and withdraw_amount <= money: #This checks if the value of withdraw_amount is one of the numbers in the list [10, 20, 30, 40, 50, 60, 70]
        money -= withdraw_amount # takes away money from the withdraw amount
        print(f"${withdraw_amount} has been taken out. New balance: {money}")
    else: 
        print("Invalid amount or insufficient funds.") # this happens if you type something thats invaid or dont have enough money 

else:
    print("Invalid choice. Please try again.") # this happens if you type something thats invaid


