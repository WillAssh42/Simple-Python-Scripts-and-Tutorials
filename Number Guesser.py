import time        # imports the time and random module
import random


print ("Welcome to the number guesser! The aim is for you to guess the random number I have selected! Each level is harder and harder! Good luck! ") # prints the text
time.sleep(1) # waits for 1 sec
number = random.randint(1,10) # makes the variable "number" equal to a number from 1-10
print("Level 1") # prints the text
time.sleep(1) # waits for 1 sec
question = input("Whats the number?") # asks for an input 

if question == number: # of the question equals the correct number then it runs the rest
    print("You got it correct!") # prints the text
    print("Level 2") 
    number1 = random.randint(1,20) # makes the varaiable "number1" equal to a number from 1-20
    time.sleep(1) # waits 1 sec
    question == input("What is the number?") # asks for an input
    
else: # if anything else is said or the wrong number, it prints "you lose"
    print("You lose")  

    if question == "number1": # if the input equals "number1" ( random.randint(1,20) ) then it runs the rest of the script
        print("You got it correct!") # prints the text
        time.sleep(1) # waits one sec
        print ("level 3 final round!") # prints the text
        number2 = random.randint(1,100) # chooses a random number from 1,100 to define number2
        question == input("What is the number") # asks for an input
        
        if question == "number2": # if the input "number2" is present it will run the rest of the script
            print("congrats you should be very pround!") # prints the text

        else:  # if anything else is said or the wrong number, it prints "you lose"
            print ("You lose")
