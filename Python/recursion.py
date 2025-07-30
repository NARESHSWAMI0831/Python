# recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

# Daily Python Practice - July 30

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")

# Creating objects
student1 = Student("Naresh", 101)
student2 = Student("Swami", 102)

# Displaying info
student1.display()
student2.display()
