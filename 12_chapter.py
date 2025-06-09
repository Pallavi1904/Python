#    #  Walrus operator

# # n = [1, 2, 3, 4, 5]
# # if (len(n) > 3):
# #     print("It's huge")

# # We can do same above thing by using walrus operator:
# if(n := len([1, 2, 3, 4, 5]) > 3):
#     print("It's huge")




#     # Type Defination in Python

# n : int = 5 #for variables
# name : str = "Pallavi Akolkar"

# def sum(a: int, b: int) -> int:
#    return a+b


#    # Type hints
# from typing import List, Tuple, Dict, Union
# # List of integers
# num: List[int] = [1, 2, 3, 4]

# # Tuple of string and int
# person: Tuple[str, int] = ("Pallavi", 12, "nom", 13, 25)

# # Dictionary of str and int
# scores: Dict[str, int] = {"Ram": 78,
#                            "Rani": 90}
# # Union
# uni: Union[int, str] = "ID1234"
# uni2 = "ID234"  # Also valid

     
#      # Match Cases
# def match_cases(status):
#    match status:
#       case 200:
#          return "OK"
#       case 404:
#          return "Not Found"
#       case 500:
#          return "Unknown status"
#       case _:
#          return "hmmmmmm"

# print(match_cases(5007))
# print(match_cases(500))
# print(match_cases(404))

   
#     # Dictionary merge and update operator: 
# dict1 = {"a":1, "b":2, "c":3}
# dict2 = {"d":1, "e":2, "f":3}
# merged = dict1 | dict2
# print(merged) 

#     # Multiple Context Manager
# with (
#    open("9_python.txt") as f1,
#    # open("12_python.txt") as f2 
# ):           #can processes on files after ):
#  print(f1.read())



#       # Exception Handling
# try:
#    a = int(input("Hey, Enter a number: "))
#    print(a)
# except Exception as e:
#    print(e)

#    # Exception Handling in chain format:
# try:
#    b = int(input("Hey, Enter a number: "))
#    print(b)
# except ValueError as v:
#    print("hyyyyy")
#    print(v)
# except Exception as e:
#    print(e)

   
#    # Raising Error
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: ")) 
# if(y == 0):
#    raise ZeroDivisionError("Hey we can't divide any number by zero")

# print(f"The division of x/y is {x/y}")

   
#    # Try with else
# try:
#    a = int(input("Enter a number: "))
#    print(a)
# except Exception as e:
#    print(e)
# else:
#    print("I am inside else")
#    #Else executes only after success of try block
   

#    # Try with Finally
# try:
#    a = int(input("Enter a number: "))
#    print(a)
# except Exception as e:
#    print(e)
# finally:
#    print("I am inside else")
#    # Try block will run wheather code succes or not
#    # Mostly usefull for functions try except blocks

  
  
#   # Global variable
# m = 89 #Global variable
# def fun():
#    m = 9 # Local variable
#    print(m)

# fun()
# print(m)

 #Uncomment above as per requirement


      # Enumerate function in python
li = [1, 2, 3, 4, 5, 6]
index = 0
for i in li:
   print(index, i)
   index += 1

# same as followed with enumerate operator:
for ind, items in enumerate(li):
   print(ind, items)


   # List comprehension
list1 = [11, 22, 33, 44, 55]
list2 = [i for i in list1 if i > 22]
print(list2)
