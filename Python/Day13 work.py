# lambda function

# Example:

"""c_to_f = lambda x: (x*9/5)+32
print(c_to_f(30))"""

# Q1:

"""a = lambda x: x*6/2*24+8
print(a(3))"""

# sort the list of dictinaries b age using a lambda function:

"""people = [{'name': 'john', 'age':28},{'name': 'mary', 'age':23},{'name': 'bop', 'age':35},{'name': 'alice', 'age':32}]

res = sorted (people, key = lambda x: x['age'])
"""

# using filter() to divied negitive num from positive num:

"""num = [-1,-2,-3,4,5,6,-7,-8,9,10]

x_pos = list(filter(lambda c: c >= 0 , num))
z_neg = list(filter(lambda c: c < 0 , num))

print("The Positive number is: ",x_pos)
print("The Negitive number is: ",z_neg)"""

# filter the lowercase string from a list:

"""c = ['dog', 'Cat', 'Giraph', 'caw' ]
res = list(filter(lambda x: x.islower(),c))
print(res)"""

# map():

"""c = [1,3,5,2,7,4,10]
res = list(map(lambda i: i**2, c))
print(res)"""

# implement a program that prompts the user to enter a list of names seperated by commas,
# use map() and a lambda function to convert each name to uppercase.

"""a = int(input(" Enter The Range You Wanted: "))
c = []

for i in range(a):
    z = input("Enter a Name: ")
    c.append(z)

res = list(map(lambda x: x.upper(),c))
print("result: ",res)"""

# calculate the sum of sequares of a list numbers using reduce() function:

from functools import reduce
 
c = [2,3,6,9]
sumseqyare = reduce(lambda x, y: x + y * y, [c[:1][0]**2] + c[1:])
print("The Sum Of Sequares Is: ",sumseqyare)