# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)



# Daily Python Practice - August 2
# Binary Search: Works only on sorted lists

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search in right half
        else:
            high = mid - 1  # Search in left half

    return -1  # Target not found

# Sorted list and target value
numbers = [5, 10, 15, 20, 25, 30, 35]
target = 25

# Search and output
result = binary_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")
