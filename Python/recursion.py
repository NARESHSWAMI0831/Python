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


# Daily Python Practice - August 6
# Linear Search with user input

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index
    return -1  # Not found

# Taking user input
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

target = int(input("Enter number to search: "))

# Search and print result
result = linear_search(numbers, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the list.")

# Daily Python Practice - August 7
# Binary Search (Iterative) - List must be sorted

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Not found

# Input from user
numbers = input("Enter sorted numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

target = int(input("Enter number to search: "))

# Search and print result
result = binary_search(numbers, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the list.")

# Daily Python Practice - August 11
# Check if a string is a palindrome

def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())  # remove spaces, punctuation
    return cleaned == cleaned[::-1]

# Input from user
user_input = input("Enter text to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("✅ Yes, it's a palindrome!")
else:
    print("❌ No, it's not a palindrome.")
