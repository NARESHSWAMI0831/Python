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



#Tuple

tup=(2,1,5,9)
print(tup[2])

#tuple sclicing
print(tup[0:2])

#tuple methods
print(tup.index(2))
print(tup.count(2))