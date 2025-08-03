# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - August 3
# Bubble Sort: Repeatedly swap adjacent elements if they are in the wrong order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample list
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Before sorting:", numbers)
bubble_sort(numbers)
print("After sorting:", numbers)
