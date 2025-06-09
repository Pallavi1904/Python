name = "Pallavi"
print(len(name))
nameshort = name[0:3]
print(nameshort)
nm = name[0:7]
print(nm)
print("##################################################################")

nameshort2 = name[-5:-2] # negative indices
print(nameshort2)
print("##################################################################")

# convert negative to positive indices
print(name[-1:-4])
print(name[6:3])
print("##################################################################")

print(name[1:5:2])
print("##################################################################")


#    String Functions
print(name.endswith("vi"))
print(name.startswith("mn")) 
print(name.count("l"))
print(name.capitalize()) # capitalize only first letter only
print(name.find("Pallavi"))
print(name.replace("Pal", "nam"))
print("##################################################################")


#Escape sequence characters

print("HII my name is pallavi \n and i am so happy") #newline

print("HII my name is pallavi \t and i am so happy") #tab

print("HII my name is pallavi \' and i am so happy") #'

print("HII my name is pallavi \\ and i am so happy") #\\
print("##################################################################")



name2 = input("Enter name: ")
print(f"Good morning {name2}")