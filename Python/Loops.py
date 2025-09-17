# loops

# while loop

# i =1
# while i <=5 :
#     print(" I can do it",i)
#     i += 1

# print(i)


# practice while loop

# 1 print 1 to 1000

# num=1
# while num<11:
#     print(num)
#     num+=1



# 2 100 to 1

# num=100
# while num>=1:
#     print(num)
#     num-=1

# 3 multiplication table

# t=1
# while t<=10:
#     print(8*t)
#     t+=1

# 4     print the element

# i=[1,4,16,25,36,49,90,31,81,100]
# idx=0
# while idx<len(i):
#     print(i[idx])
#     idx+=1

# 5 serch of tuple

i=(1,4,16,25,36,49,90,31,81,100)

x=36
z=0
while z<len(i):
    if(i[z]==x):
     print("found",z)
     break
    else:
       print("finding..")
    z+=1



# Break and Continue

i=0
while i<=10:
    if(i%2 ==0):
       i+=1 
       continue 
    print(i)
    i+=1
    

# for loop
# array

num=[1,56,89,45,67,455,45,67]

# output
