     # Dictionary

marks = {
    "kiara":100,
    "harry":23,
    "pallavi":100,
    "naman":90,
    0:"harry"
}

print(marks, type(marks))
print(marks["pallavi"])

#Dictionary Methods
print(marks.items())# provides all key-value pair of marks
print(marks.keys()) #providing all keys of marks

marks.update({"kiara":"89"}) #Updating value
print(marks)
marks.update({"friend":"priya"}) #If key not present then update or add it in dictionary
print(marks)


print(marks.get(0)) #Get value at given 0 key
print(marks[0]) #provides error

# there is diff between .get method and normal accesing of that key as above
# they both provide same value but after giving incorrect value .get() method provides
# none and other give error
#example:
#Asked in interview..............
print(marks.get("pallavi2")) #gives none
# print(marks["pallavi2"])     #gives error 


    # Sets
d = {} #Empty dictionary

d2 = {
    "kiara":100,
    "harry":23,
    }  #Dictionary

m = set() #Empty set
# Dont use M ={ } as empty set as it is empty dictionary Interview.......!


m1 = {12, 3, 22, 1, 15}
print(m1, type(m1))

#Set Methods
print(len(m1)) #returns length of set

m1.remove(1) #remove given element
print(m1)

m1.add(16) #adds given element
print(m1)

m1.pop() #remove random element from set
print(m1)

m1.clear() #Remove all elements in set i.e empty the set
print(m1)

# Union and Intersection in set

s1 = {12, 14, 26, 10}
s2 = {12, 15, 17, 10}

print(s1.union(s2)) #provides all values in both sets but common values present single in set s1 and s2

print(s1.intersection(s2)) #provides common values in set s1 and s2





