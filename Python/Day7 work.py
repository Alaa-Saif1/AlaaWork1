# use extend():

"""x = [1,2,3]
x.extend([4,5])
print(x)"""

# use join():

"""x = ['1','2','3']
for i in x:
    v = "|".join(x)
print(v)"""

# comprehension:

"""result = []
result = [i**2 for i in range(5)]
print(result)

res = []
for i in range(5):
    res.append(i**2)
print(res)

########

res3 = []
for i in range(5):
    if(i % 2 == 0):
        res3.append(i)
print(res3)

res4 = []
res4 = [i for i in range(5) if i % 2 == 0]
print(res4)"""

# Our task is to analyze whether a die is fair by counting how often each value (1, 2, 3, 4, 5, 6) appears:

"""def countInput(s):
    counters = [0] * (s + 1)
    for i in range(s):
        r = int(input("Enter the number of roll: "))
        if r <= 6:
            counters[r] = counters[r] + 1     
    return counters
        
def printCounters(counters):
        #for i in counters :
            counter = [i for i in counters if i * i != 0]
            print(counter)
      
def main():
    s = int(input("Enter the number of sides: "))
    counters = countInput(s)
    printCounters(counters)
main()"""

# create table:

"""COUNTRIES = 3 #col
MEDALS = 2 # row
counts = []

for i in range(MEDALS): # row
    for j in range(COUNTRIES): # col
        row = [] * COUNTRIES
        counts.append(row)
        print(counts, end = " ")
print()"""

# Found a name of persone whos age > 22:

"""dec1 = {1: {"name" : "p1",
            "age" : 22},
        2: {"name" : "p2",
            "age" : 27}}

for key in dec1:
    x = dec1[key]["age"]
    if(x > 22):
        print(dec1[key]["name"])"""