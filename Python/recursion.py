# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# Daily Python Practice - July 29

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    return reversed_num

# Sample test
number = 12345
print(f"Original Number: {number}")
print(f"Reversed Number: {reverse_number(number)}")

