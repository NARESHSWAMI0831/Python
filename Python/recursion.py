# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# Daily Python Practice - July 31

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")

# Derived class
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show_details(self):
        self.show()
        print(f"Roll Number: {self.roll_no}")

# Creating an object of Student
s1 = Student("Naresh", 101)
s1.show_details()

