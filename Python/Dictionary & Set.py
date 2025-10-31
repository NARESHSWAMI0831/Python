# Dictionary
#Basic

info={
    "name":"alok",
    "suhbject": {
        "che":5,
        "bio":6,
        "math":9,
        "eng":8
    }
    
}
print(info["suhbject"]["math"])


# Dictionary Method


# 1 return all keys

print(len(list(info.keys())))   #typecast,length

# 2 return all values

print(info.values())

# 3 return all

print(list(info.items()))

# 4 return the key according to value

print(info.get("name"))

# 5 insert the spefics item to the dictionary

info.update({"city" : "delhi"})
print(info)



#SET
collection={1,2,3,4,5,6,7,8}
print(collection)
print(type(collection))  #type


# SET METHODS

# 1 adds an element

collection.add("hello")
print(collection)

# 2 removes the element

collection.remove(2)
print(collection)

# 3 removes a randown value


print(collection.pop())

# 4 empties the set

collection.clear()
print(collection)

# 5 combine both set values & return new

set1={1,5,8,6,0}
set2={2,3,4,6,7}
print(set1.union(set2))

# 6 combine common values & return new 
print(set1.intersection(set2))


# PRACTICE

# 1
word={"table":["a furniture","list of fact and figure"],
        "cat":"a small animal"}
print(word)
# 
# 
