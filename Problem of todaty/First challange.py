number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))
number3 = float(input("Enter Third Number: "))
larges_Num = number3

if number1 == number2 == number3:
    print("All Numbers Are Equal.")
elif (number1 >= number2) and (number1 >= number3):
   larges_Num = number1
elif (number2 >= number1) and (number2 >= number3):
   larges_Num = number2
else:
   larges_Num = number3

print("The largest number is", larges_Num)
