
num = [1,4,5,7,3,0]

for i in range(len(num)):
    current_number = num[i]
    is_greater = True

    for j in range(i + 1, len(num)):
        if current_number < num[j]:
            is_greater = False
            break

    if is_greater:
        print(current_number)
          