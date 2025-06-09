   # Lists
   
friends = ["Apple","pallavi",False,23,45.78,True,"naman"]
  
   #Accesing list items
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
print(friends[6])

# Lists are mutable
friends[0]="Priya"
print(friends[0])

#List slicing
print(friends[0:3])

#List methods
friends2 = [2,35,22,34,89,1]
(friends2.sort()) #sort in ascending order
print(friends2)

(friends2.reverse()) #sort in descending order
print(friends2)

(friends2.append(8)) #append 8 add end of list
print(friends2)

(friends2.insert(3,10000)) #insert 10 at index 3
print(friends2.pop(2))
print(friends2)

(friends2.pop(2)) #remove element at index 2 and return element
print(friends2)

(friends2.remove(89)) #remove element 89 from list
print(friends2)


  #    Tuple

l2 = (1,1,1,13,24,1,23,4)
a=() #Empty tuple
a2=(1,) #Tuple with single element need to give a comma

print(l2)
print(l2.count(1)) #return no of occurances of 1
print(l2.index(1)) #returns index of 1st occurance of 1
print(l2.index(24)) #returns index of 1st occurance of 24




