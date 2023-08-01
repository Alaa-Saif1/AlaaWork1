# stack:
# --- Way One:

"""stack = []

stack.append('H')
stack.append('E')
stack.append('L')
stack.append('L')
stack.append('O')


print("The reverse of the word is: ")
print(stack.pop(), end= " ")
print(stack.pop(), end= " ")
print(stack.pop(), end= " ")
print(stack.pop(), end= " ")
print(stack.pop(), end= " ")"""

# Second Way:

"""class Stack:
    def __init__(self):
        self.a = []
        
    def push(self,stack):
        self.a.append(stack)
    
    def pop(self):
        peek = self.a[-1]
        self.a.remove(peek)
        return peek
    
stack = Stack()

Word = input("Enter Any Word You Need It: ")

for i in Word:
    stack.push(i)
    
print("The Normal word is: \n",stack.a)
print("The Reverse word is: ")

for i in range(len(stack.a)):
    print(stack.pop(), end= " ")"""
   
# Queues:

# change stack exprission to prefix:












 
 