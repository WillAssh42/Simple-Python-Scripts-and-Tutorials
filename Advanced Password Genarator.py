# password genarator ( numbers only )
import random # imports random module
print("Welcome To The Passoword Genarator") # prints the text
   amount = input ("How Many Numbers Long Should it be? (1-6 digits)") # asks for an input from the user 
if amount == "1":
        print (random.randint(1,9)) # prints the random number from 1,9
elif amount == "2":
        print(random.randint(10,99)) # prints the random number from 10,99
elif amount == "3":
        print(random.randint(100,999)) # prints the random number from 100,999
elif amount == "4":
        print (random.randint(1000,9999)) # prints the random number from 1000,9999
elif amount == "5:":
        print (random.randint(10000,99999)) # prints the random number from 10000,99999
elif amount == "6":
        print(random.randint(100000,999999)) # prints the random number from 100000,99
else: # if anything but the numbers 1-6 used then it prints "invalid answer" and restarts
        print ("invalid answer") 
        
