marks=[56,46,90,78,66]  #list
print(marks)
student=["alok",67,"delhi"]
student[0]="yash"
print(student)

print(marks[:1])  #slicing


#List Methods

table=[1,3,4,5,3,8]
table.append(12)
table.sort()
table.sort(reverse=True)
table.reverse()
table.insert(1,2)
table.remove(3)
table.pop(0)
print(table)



# Tuple

tup=(2,1,5,9)
print(tup[2])

#tuple sclicing
print(tup[0:2])

#tuple methods
print(tup.index(2))
print(tup.count(2))





# Daily Code: August 25, 2025
# Program to find the largest number in a list

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
nums = [12, 45, 78, 34, 89, 23]
print("List:", nums)
print("Largest number in the list:", find_largest(nums))


# Daily Code: August 26
# Program to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")


# Daily Code: August 27
# Program to find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")




# Daily Code: August 27
# Program to find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")





# Daily Code: August 29
# Program to check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")



# Daily Code: August 30
# Program to find factorial of a number using loop

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")




# Daily Practice: September 6, 2025
# Program to check if a number is Prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a Prime number ✅")
else:
    print(f"{number} is NOT a Prime number ❌")

