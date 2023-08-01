from collections import Counter

def print_most_frequent_num(numbers):
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    if most_common:
        frequent_number, frequency = most_common[0]
        print(f"The Most Frequent Number Is {frequent_number}")
    else:
        print("The list is empty.")

numbers = [1,8,7,4,1,2,2,2]
print_most_frequent_num(numbers)