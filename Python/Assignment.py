def bubble_sort(a):
    n = len(a)
    for i in range(n - 1): # to pass through all list element.
         for j in range(n-i-1): # last i are in place from first.
             if a[j] > a[j+1]:
                 a[j], a[j+1] = a[j+1], a[j]
                 
def selection_sort(a):
    n = len(a)
    for i in range(n): # to pass through all list element.
        min_index = i # find the minimum element.
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i] # swap the minimum with the first element.
   
def quick_sort(a):
    if len(a) <= 1: # to checked if the list is empty!
        return a
    
    pivot = a[0] # how we choose the pivot element and partition the ist inot two  sub-list.
    less = [x for x in a[1:] if x <= pivot]
    greater = [x for x in a[:1] if x > pivot]
    
    return quick_sort(less) + [pivot] + quick_sort(greater) # concatenated the sorted result with pivot to do final sorted.
   
while True:
    try:
        lst = input("Enter a list of numbers: ").split(" ")
         
        a = input("Choose The Sorting Algorithm (Bubble,Selection,Quick) or press 'e' To Exict: ")
        
        if a == 'e':
            break    
        if a == 'Bubble':
            bubble_sort(lst)
        elif a == 'Selection':
            selection_sort(lst)
        elif a == 'Quick':
            quick_sort(lst)
        else:
            print("Wrong Choice!!")
            continue
        print("Sorted list:", lst)
        print()
            
    except ValueError:
        print("Wrong Input!!")
        continue
        
        