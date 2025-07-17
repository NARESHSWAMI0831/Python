"""A=10
B=20
C=A+B
print(C)
# A,B,C are the variable
# Variable is a name assign to a memory 

X=10 # integer
Y="10,yes" #string
Z=10.51 #Float
W="true false" #Bollean
V= "none" #none
#These are the data type in pyhton

#Operator

a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
#arithmetic ope

a=50
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#relational / comparison ope

num=10
num= num+10
num+=10
print(num)
#example of assignment ope

a=50
b=30
print(not False)
print(not (a>b))
#example of logical ope

a=2 #int
b=4.25 #float
print(a+b) #ans float
#type coversion

a=int("2")
b=4.25
print(a+b)
#type casting

name=input("enter your name :")
print(name)
#input from user



#Question Practice

#1 Write a program to input 2 number & print their sum

num1=int(input("enter your number 1 :"))
num2=int(input("enter your number 2 :"))
sum=num1+num2
print(sum)


#2 WAP to input side of a square & print its area

side=float(input("enter your side :"))
area=side*side
print(area)

#3 WAP to input 2 floating point number and print their average

first=float(input("enter your number 1 :"))
second=float(input("enter your number 2 :"))
average=(first+second)/2 ##
print(average)"""


#WAP to input 2 int numbers,a and b
#print true if a is greater than or equal to b.if not print false

a=int(input("enter your number 1 :"))
b=int(input("enter your number 2 :"))
print(a>=b)