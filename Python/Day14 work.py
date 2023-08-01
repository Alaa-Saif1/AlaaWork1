# iter()

"""lst = [1,2,3]
   
v = iter(lst)
print(next(v))"""

# Generation

"""def fun1():
    yield 1
    yield 2
    yield 3
    
v = fun1()
print(next(v))
for i in v:
    print(i) """

#

"""def fibonacci_numbers(nums):
    x, y = 0, 1
    for i in range(nums):
        x, y = y, x+y
        yield x
        
def square(nums):
    for num in nums:
        yield num**2
        
def a(nums):
    for num in nums:
        yield num**3
        
print(sum(a(square(fibonacci_numbers(10)))))"""

# you are given a list of numbers from 1 to 15,write a generator function that generate a sequence of
#even numbers from the list.

"""def even_numbers(lst):
    for i in lst:
        if i%2 == 0:
            yield i
            
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

v = even_numbers(lst)
for i in v:
    print(i)"""

# wrapper function

"""def func1(fun):
    def wrapper():
        print("Hello")
        fun()
        print("Welcome to Python")
    return wrapper
 
@func1
def func2():
    print("Code Academy")
    
func2()"""

# Decorator with parameters:

"""import time
import math

def calculate_time(func):
    def wrapper(n):
        begin = time.time()
        func(n)
        end = time.time()
        print("time taken in : ",
              func.__name__, end - begin)
    return wrapper
    
@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)"""
