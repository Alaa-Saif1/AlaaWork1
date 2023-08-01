def square(r, h):
    volume = 3.14159 * r * r * h
    squared_volume = volume ** 2
    return squared_volume
 
result = square(10,5)
print("The squared volume is:", result)