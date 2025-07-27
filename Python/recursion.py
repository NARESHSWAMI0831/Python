# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


# Daily Python Practice - July 27

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("Please enter valid numbers only.")

finally:
    print("This block always runs, no matter what!")

