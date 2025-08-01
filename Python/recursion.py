# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - August 1
# Linear Search: Check if an element exists in a list

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the element is found
    return -1  # Return -1 if not found

# Sample list and target
numbers = [10, 20, 30, 40, 50]
target = 30

# Function call
result = linear_search(numbers, target)

# Output
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")

