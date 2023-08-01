# See The Diffrent resulet when we write the equation with/ without pracet:
b = 2
r = 50
n = 1

res1 = b*((1+r/100)**n)
print("res1=" ,res1)

res2 = b*1+r/100**n
print("res2=", res2)

# How to use the Opreater:
#1) 
baisas = 1729
omr = baisas // 1000
baisas = baisas % 1000
print ("I HAVE", omr, "OR AND", baisas, "baisas")

#2)
price = 4.35
quan = 100
total = price * quan
print(round(total))

#3) Print the result with two number of digit:
x = 434.99999
x = int(x * 100) / 100.0
print(x)


# python program to calculate the total surface volume and area of a cylinder:
h = 4
r = 6
pi = 3.14

volume = pi * r**2 *h
print(volume)

Area = (2 * pi * r**2) + (2 * pi * r * h)
print(format(Area, ".2f"))

# idf someone bought 10 tons of iron where the value of one ton is one rial.write a program that calculate 
# the total cost of purchase with an addition of 5% var.
a = 10
b = 1

res1 = a * b
print(res1)

addition = 5/100

res2 = res1 * addition
print(res2)

finall_cost = res1 + res2
print(finall_cost)


