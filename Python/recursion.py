# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - August 4
# Selection Sort: Repeatedly find the minimum element and move it to the front

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first unsorted element is the minimum
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Sample list
numbers = [29, 10, 14, 37, 13]

print("Before sorting:", numbers)
selection_sort(numbers)
print("After sorting:", numbers)

