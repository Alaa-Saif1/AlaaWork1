# Find Year of Leap Year:

"""year = int(input("Enter Year: "))

if (year % 4 == 0 or year % 400 == 0) :
    print(year, "Is Leap year")
else:
     print(year, "Is Not Leap year")"""
        
# check if you can stor filse in the memory if it has a space:

"""x = int(input("Enter storage: "))
n = int(input("Enter number of file: "))
y = int(input("Enter weight: "))

mlti_of_n_y = (n * y)

if mlti_of_n_y <= x:
    print("User Can Find Space In The Memoy")
else:
    print("User Can Not Find Space In The Memoy")"""

# check if 10:30 come before 11:00 :

"""hour1 = int(input("Enter hour1: "))
hour2 = int(input("Enter hour2: "))
min1 = int(input("Enter min1: "))
min2 = int(input("Enter min2: "))

if (hour1 > hour2):
    print("houer 1 come first")
else:
    if(hour2 == hour2):
        if(min1 > min2):
            print("houer 1 come first")
        else:
            print("houer 2 come first")
    else:
        print("houer 2 come first") """

# Find middle character from given string, but if it is even reslt should be 2 character:

"""text =input("Enter text: ")
text_lenght =len(text)

Middle= text_lenght //2

if (text_lenght % 2 == 0):
    print("Middle character of the string :",text[Middle -1 : Middle + 1])
else:
     print("Middle character of the string :",text[text_lenght //2])"""

# Other Slution:

"""def middle_char(text):
  return text[(len(text)-1)//2:(len(text)+2)//2]
text = "car"
print("string: ",text)
print("Middle character of the string: ",middle_char(text))
text = "cars"
print(" string: ",text)
print("Middle character of the string: ",middle_char(text))"""

# calculate the temperature degree in celsius or fahrenheit. if it is celsius, transfer it to fahrenheit and vice versa.

"""Temp = float(input("Enter temperature : "))
Degree = input("Enter Degree: ")

fahrenheit = ((Temp * 5/9) + 32)
celsius = ((Temp - 32) * 5/9)

if (Degree == "C"):
    print("Temp in: ",celsius)
else:
   print("Temp in: ",fahrenheit)"""
    
# Write a program that print the first 10 even numbers using while loop:

"""x = int(input("Enter number: "))
i = 0

while i <= x:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1"""

# write a program that prints the first 10 numbers and their squares using while loop:

"""a = 1
i = 1

while i <= 10:
    if i <= a:
        print(i*i)
        a+= 1
        i+=1"""
    
# write while loop that prints the following sequence(105,98,91,...,7):

"""i = 105
while i >=7:
    print(i)
    i-=7"""

# Convert string to Ascii:

wrd = str (input("write the word: "))
str=0
length = len(wrd)
while(str < length):
    print(ord(wrd[str]))
    str = str + 1
    
    
    

    
    
         




