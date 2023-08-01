# Suppose the input file contains salary and name data as a single line of text (Average of salaries,Name with highest salary):

"""inputFile = open("txt.txt", "r")


salary = 0
highest = {}
i= 0

for line in inputFile:
    data = line.split(" ")
    salary += float(data[0])
    highest[data[1].rstrip()] = float(data [0])
    i = i + 1
    average = salary / i
h = []
for key, value in highest.items():
        h.append(value)     
    
for key,value in highest.items():
        if value == max(h):
            print(key,value)
     
    
inputFile.close()"""

# Q1:

"""inputFile = open("q1.txt", "r")

Distance = {}

for line in inputFile:
    data = line.split(" ")
    speed = int(data[0])
    time = int(data[1])
    
    Distance = speed * time
    print(Distance)
    

inputFile.close()"""

# Q2:

"""inputFile = open("q2.txt", "r")

factor = []

for line in inputFile:
    num = int(line)
    for i in range(1,num+1):
        if num % i == 0:
            factor.append(i)
print(factor)
    
inputFile.close()"""

# Q3:

"""inputFile = open("q3.txt", "r")

maxcount = 0
num_of_max_freq = 0

for line in inputFile:
    data = line.split(" ")
    n = int(data[0])
    for i in range(0, n):
        count = 0
        for j in range(n, 0):
            if([i] == [j]):
                count += 1
                if(count > maxcount):
                    maxcount = count
                    num_of_max_freq += i
        print(num_of_max_freq)
        
inputFile.close()"""

# Q4:

"""inputFile = open("q4.txt", "r")

mlti_of_n_y = []

for line in inputFile:
    data = line.split(" ")
    s = int(data[0])
    f = int(data[1])
    w = int(data[2])
    
    mlti_of_n_y = (f * w)
    if mlti_of_n_y <= s:
        print("Yes")
    else:
        print("No")
   
inputFile.close()"""

# Q5:

"""inputFile = open("q4.txt", "r")

hcf = []

for line in inputFile:
    data = line.split(" ")
    x = int(data[0])
    y = int(data[1])
    
    while(y):
        hcf = y, x % y
        return(hcf)
    print(hcf)
        
inputFile.close()"""




        
        
        

    
    
