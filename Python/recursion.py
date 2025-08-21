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



# number_guessing_game.py

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! 📉")
            elif guess > number_to_guess:
                print("Too high! 📈")
            else:
                print(f"🎉 Correct! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
    # yes
   

   import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()



# Daily Python Practice - August 14
# Find all prime numbers in a user-given range and save them to a file.

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

start = int(input("Start of range: "))
end = int(input("End of range: "))

primes = [x for x in range(start, end + 1) if is_prime(x)]
print("Primes:", primes)

filename = f"primes_{start}_{end}.txt"
with open(filename, "w") as f:
    f.write(", ".join(map(str, primes)))

print(f"✅ Saved {len(primes)} primes to {filename}")


# Daily Python Practice - August 15
# Reverse a string using slicing and loop methods.

text = input("Enter a string: ")

# Method 1: Slicing
reversed_text_slice = text[::-1]
print("Reversed (slicing):", reversed_text_slice)

# Method 2: Loop
reversed_text_loop = ""
for char in text:
    reversed_text_loop = char + reversed_text_loop
print("Reversed (loop):", reversed_text_loop)

# Armstrong number checker
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")




# Program: Palindrome Checker
# Date: August 17, 2025

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
text = input("Enter a word or phrase: ")
if is_palindrome(text):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")




# Daily Code: August 18
# Program to check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a Prime number.")
else:
    print(number, "is NOT a Prime number.")


# Daily Code: August 19
# Program to print Fibonacci series using recursion

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Example usage
terms = int(input("Enter number of terms: "))
print("Fibonacci series:", fibonacci(terms))


# Daily Code: August 20
# Program to find the largest element in a list

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
nums = [12, 45, 23, 67, 89, 34]
print("Numbers:", nums)
print("Largest number is:", find_largest(nums))



# Daily Code: August 21
# Program to generate Fibonacci sequence using recursion

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    seq = fibonacci(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq

# Example usage
n_terms = 10
print(f"Fibonacci sequence with {n_terms} terms:")
print(fibonacci(n_terms))

# Daily Code: August 22
# Program to find prime numbers in a given range

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
start = 10
end = 50
print(f"Prime numbers between {start} and {end}:")
print(prime_in_range(start, end))
