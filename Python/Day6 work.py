# write a function that compute the sum of the digits in an integer.Use the following method header:
# for example, sum_digits(234) return 9 (2+3+4).write a test program that prompts the user to enter an integer and display
# the sum of all it is digits.

"""def sum_digits(n):
    
    sum = 0
    for i in str(n): 
      sum += int(i)      
    return sum
   
n = input("Eter an integer number: ")
print(sum_digits(n))"""

# write a function that return the area of a regular polygon using the following header:

"""from math import tan, pi



def area_of_regular(n_sides,s_length):
    area= n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
    return area

n_sides = int(input("Enter the number of sides: "))
s_length = float(input("Enter the side: "))        
print("the area of the polygon: ",area_of_regular(n_sides,s_length))"""

# write a function def countVowels(string) that returns a count of all vowels in the string:


"""def countVowels(text):
    count = 0
    i = 0
    for i in text:
        if((i in ['a','e','i','o','u']) or (i in ['A','E','I','O','U'])):   
            count = count +1
    return count

e = input("count number of all vowels in the string: ")
print("the count vowels is : ",countVowels(e))"""

# Define a list of integers containing the first five prim numbers:

"""prim_n = [2,3,5,7,11]
print(prim_n)"""

# Write for loops that iterate over the elements of a list without the use of the range function for the following tasks.
#a. Printing all elements of a list in a single row, separated by spaces.
#b. Computing the product of all elements in a list.
#c. Counting how many elements in a list are negative.

"""from operator import*

list = [22,3,-2,-1,10,1]
res = 1
neg_count = 0
for element in list:
    print(element, end= " ")
    res = mul(element, res)
    if element <= 0:
        neg_count += 1
print()
print("computing the product of all elements: ",res)
print("Negative numbers in the list: ", neg_count)"""






    

    

  
    