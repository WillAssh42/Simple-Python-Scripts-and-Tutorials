# lets do some more advanced python, were going to make a choice selection, so when you type an answer something happens but if you choose something else, someting else happens. 

import time  # this is a module that allows us to use time functions
print("Welcome! Here you choose the red pill or the blue pill") # this prints the question 

answer = input("red or blue: ") # this prints the question and makes you type an answer before printing the outcome

if answer == "red": # this is one answer choice
    print("you died")
elif answer == "blue": # this is the other   
    print(" you died")
else:
    print("Invalid choice.") # this will only happen if you put something invalid
