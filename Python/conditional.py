#STRINGS

"""Basic operations"""

# Concatenation

"""firstname=input("enter your first name :")
lastname=input("enter your last name :")
fullname= firstname+lastname
print(fullname)"""


#Length of str

"""firstname="kajudi"
print(len(firstname)) #tell the length

#Indexing (start from 0)

print(firstname[0])"""

#Slicing

"""print(firstname[:-1])"""

#Basic function of str

a="i am studing python in my self study"

"""print(a.endswith("dy")) """ #return true if string end with substr

"""print(a.capitalize()) """  #capitalize 1st char

"""print(a.replace("t","k")) """ #replace old to new

"""print(a.find("in")) """   #find first occurance

"""print(a.count("t"))"""     #count the occurance


""" Question Practice"""

#1 WAP to input user's first name & print its length

"""firstname=input("enter your first name :")
print("Length of your name is :",len(firstname))"""

#2 WAP to find the occurrence of $ in a string

"""a="find the occurrence of $ in this"
print(a.count("$"))"""


#CONDITIONAL Statements

light="black"
if(light=="green"):    #if always check the condition
    print("go")
elif(light=="red"):  #elif check only if is false
    print("stop")
elif(light=="yellow"):
    print("ready")
else:                  # when all previous condition false than this final condition appear
    print("jumped")


# Nesting

age = 34
if(age >= 18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive") 




#Practice Question

#1 Grade student based on marks

"""Marks=int(input("enter marks :"))
if(Marks >= 90):
    print("grade = 'A'")
elif(90>Marks>=80):
    print("grade = 'B'")
elif(80>Marks>=70):
    print("grade = 'C'")
else:
    print("grade = 'D'")  """         
     


#2 WAP to check if a number entered by user is odd or even

"""num=int(input("enter num"))
if(num / 2 ==0):
    print("num is even")
else:
    print("num is odd")    

    
#3 WAP to find the greatest of 3 number entered by the user

num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if(num1>=num2 and num1>=num3):
    print("num1 is the greatest one")
elif(num2>=num1 and num2>=num3):
    print("num2 is the greatest one")
elif(num3>=num1 and num3>=num2):
    print("num3 is the greatest one")"""



#4 wap to check if a number is a multiple of 7 or not


num1=int(input("enter num1"))

if(num1 % 7 ==0):
    print("multiple of 7")
else:
    print("not a multiple")




