# Phone formate:

"""string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0

while valid and position < len(string) :
    if position == 0:
       valid = string[position] == "("
    elif position == 4 :
         valid = string[position] == ")"
    elif position == 8 :
         valid = string[position] == "-"
    else:
        valid = string[position].isdigit()
    position = position + 1
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")"""
    
# write a python program where the ser enters a password and check if the password is vaild or not:

"""string = input("Enter password here: ")
l = 0
u = 0
n = 0
s = 0

if len(string) >= 8:
    for position in string:
        if position.islower():
            l+= 1
        if position.isupper():
            u+= 1
        if position.isdigit():
            n+= 1
        if (position in '@$#_'):
            s+= 1
        
if (l >= 1 and u >= 1 and n >= 1 and s >= 1 and l+u+n+s == len(string)):
    print("The Password is vaild")
else:
    print("The Password is invalid")"""
            
# check random():

"""import random 

print(round(random.random()*100,2))"""

# Solve a game, guess a number between 1 and 100:

"""from random import randint

rand = randint(1,100)
n = False

while not n:
    UrGuess = int(input("Enter Number from 1 to 100: "))
    if UrGuess < 1 or UrGuess > 100:
        print("Your guess is outside range 1-100!")
    else:
        if UrGuess == rand:
            print("Is Correct!")
            n = True
        elif UrGuess > rand:
            print("Go Lower")
        else:
            print("Go Hiher")"""

# how to use countinue and break:

"""for i in range(1,10):
    print(i)
    if (i == 5):
        print("We skip number 5!")
        continue
    else:
        if(i == 6):
            print("go out of loop")
            break"""
            
        
        
           