# print value inside table:

"""COUNTRIES = 3 
MEDALS = 2

c = [[i] * 3 for i in range(3)]

for i in range(COUNTRIES):
    for j in range(MEDALS):
        c[i][j] = i + 3
        c[i][j] = j * 3
        print(c, end = " ")
    print():"""


# create table:

"""x = [[1,2,3],
     [4,5,6]]

for i in range(2):
    for j in range(3):
        print(x[i][j], end= " ")
    print()"""

#  create [1,1,1
#          2,2,2,
#          3,3,3]

"""n = [[i] * 3 for i in range(1,4)]

for i in range(3):
    for j in range(3):
        print(n[i][j], end= " ")
    print()"""

# write a program where the user determines the number of rows and columns,then take input from user for each row, and
# column as a 2d list.Finally, print the table of the 2d list

"""row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

t = []
print("Enter the entrise row: ")

for i in range(row):
    n = []
    for j in range(col):
        u = n.append(int(input()))
        t.append(n)
        
for i in range(row):
    for j in range(col):
        print(t[i][j], end= " ")
    print()"""

# Write a 2d list that print te following:   1000
#                                            2100
#                                            2210
#                                            2221

"""arr = [[i] * 4 for i in range(4)]
for i in range(4):
    for j in range(4):
        if [i] == [j]:
            arr[i][j] = 1
        elif [i] < [j]:
            arr[i][j] = 0
        elif [i] > [j]:
            arr[i][j] = 2
print(arr, end= " ")
print()"""

# write a 2d list that print the following: 1000, 0101, 1010, 0101:

"""num = 4
arr = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            arr[i][j] = 1

for i in range(num):
    for j in range(num):
        print(arr[i][j], end= " ")
    print()"""
        
               
    

            





