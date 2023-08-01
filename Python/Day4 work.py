# check how for loop printting:

"""stateName = "Virginia"
for letter in stateName:
    print(letter, end='')"""
    
# Average Example:


"""Total = 0
num = int(input("Enter number of value: "))

for i in range (1,num + 1):
    string = int(input("Enter value: "))
    Total = Total + string
    
if num> 0:
    avg = Total / num
    print(avg)
else:
    avg = 0
    print(avg)"""

# print the following pattern of brackets [][][]:

"""for i in range(3): #number of rows
    for j in range(4): #number of colomns
        print("[]", end="")
    print()"""

# Q1:
 # write a program code to decrepit the message to git the original:

"""message = "|rx#duh#juhdwh"

for i in message:
    m = ord(i) - 3
    n = chr(m)
    print(n, end='')"""
  
# print all perfect number from 1 to 100, if you know that a prefect number is a positive integer that is equal to the sum of th is positive divisors,excluding that number
# itself.For instance, 6 has divisors 1,2 and 3 (excluding itself), and 1+2+3 = 6, so 6 is perfect number.


n = 0
for i in range(2, 101):
    n = 0
    for j in range(1,i):
        if i % j == 0:
            n = n + j
    if i == n:
        print(i)
    
    
     

            
         
        
   
 


