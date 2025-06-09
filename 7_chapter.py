 # Loops

# 1]For loop
for i in range(4): #automatically goes 0 to 4
    print(i)

l = [1, 7, 8]
for items in l:
    print(items)    


# 2]While loop
i=1
while(i<6):
    print(i)
    i +=1  

#range in python
for i in range(0, 50, 10):
 print(i)  

# For loops with else
l2 = [111, 222, 333, 444]
for items in l2:
    print(items)
else:
    print("Done") 

#Break statement
for i in range(0, 21):
    print(i)
    if(i == 10):
        break   

# Continue statement
for i in range(10):  # No unnecessary spaces before 'for'
    if i == 5:  # Consistent indentation (4 spaces)
        continue  # Same indentation level as 'if'
    print(i)  # Same indentation level as 'if' block


# Pass statement
l3 = [1, 2, 3, 4]
for items in l3:
    pass



    # Questions


#print Table of 7
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# Factorial using user input
n = int(input("Enter the Number: "))
product = 1
for i in range(1, n+1):
    product = product*i 
print(f"Factorial of {n} is {product}")


 # Star pattern
#   *
#  ***
# ***** 
n = int(input("Enter the Number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="") # provides space without new line due to end=""
    print("*"* (2*i-1), end="")# provides times of start after spaces
    print("") # now provide line



# Star pattern
# *
# **
# *** 
n = int(input("Enter the Number: "))
for i in range(1, n+1):
    print("*"* (i), end="")
    print("")     

# Star pattern
# ***
# * *
# *** 
n = int(input("Enter the Number: "))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")

#Print a table in reverse order
n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11-i)}")