def multiples(num, length):
    multiples1 = []
    count = 1

    while len(multiples1) < length:
        multiples1.append(num * count)
        count += 1

    return multiples1
   
res = multiples(3, 7)
print(res)