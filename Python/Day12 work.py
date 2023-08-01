# Binary Search Algorithm:

# Q1:

"""def Binary(list1, lindex, hindex, x):
    if hindex >= lindex:
        mid = (hindex + lindex) // 2
        if list1[mid] == x:
            return mid
        
        elif list1[mid] > x:
            
            return Binary(list1, lindex, mid - 1, x)
        else:
            return Binary(list1, mid + 1, hindex, x)
    else:
        return - 1

    
list1 = [1,5,15,20,25,30,35,40,45]
x = 25

res1 = Binary(list1,0,len(list1)-1, x)
print("The Element is: ", str(res1))"""

# Q2:
# square root: given a non-negative integer 'x'm compute and return the square root of 'x'.implement the solution using
# bainary search.

"""lis1= [1.0,2.0,3.5,4.0,5.0,6.0,7.0,8.0,9.0,10.0]

x = int(input("Enter any element you wanted: "))

k = x ** 0.5
n = len(lis1)
lindex = 0
hindex = n - 1

while lindex <= hindex:
    mid = (lindex + hindex) // 2
    
    if lis1[mid] == k:
        print("Success :",k)
        break
    
    elif lis1[mid] > k:
        lindex = mid + 1
        
    elif lis1[mid] < k:
        hindex = mid - 1
        
    else:
        print("Unsuccess: ", k)
        break"""

# Insertion sort implementation

"""def Sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
            arr[j + 1] = key
      
x = [5, 4, 10, 16]
print("Unsorted Array Is: ",x)

Sort(x)
print("Sorted Array Is: ",x)"""

# Q1:

"""def Sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
        while j >= 0 and int(key.split(",")[1]) < int(arr[j].split(",")[1]):
            arr[j + 1] = arr[j]
            j = j - 1
            
            arr[j + 1] = key
      
x = ["Said,25", "Majid,19", "Salim,32", "Ali,21", "Sultan,28"]
Sort(x)
y = [i.split(",", 1)[0] for i in x]
print("The Sorted Array Is: ",y)"""


#write a program that has the three sort algorithms implemented with the user entering the list and choosing which sorting
#algorithm they want to use.The program stops when the ser wants it to stop.
        
