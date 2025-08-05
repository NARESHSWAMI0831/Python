# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - August 5
# Insertion Sort: Build the sorted list one item at a time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Sample list
numbers = [12, 11, 13, 5, 6]

print("Before sorting:", numbers)
insertion_sort(numbers)
print("After sorting:", numbers)
