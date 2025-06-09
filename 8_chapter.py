# Function

def avg():  #Function defination
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    c = int(input("Enter num 3: "))
    result = (a+b+c)/3
    print(result)
avg()  #Function call


# Functions with arguments
def greet(name):
    print(f"Good Morning {name}")
greet("Pallavi")



#Function with default argument
def greet2(name="Priya"):
    print(f"Good Morning {name}")

greet2() #Default value come
greet2("Pallavi") #pallavi come


#Recursive Functions
def factorial(n):
    if(n ==1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(6))
print(factorial(1))


#Find greatest of 3 number using function
def greatest(a, b, c):
    if(a>b and a>c):
        printf("a is greatest")
    elif(b>a and b>c):
        printf("b is greatest")
    else:
        print("c is greatest")
print(greatest(10, 12, 14))


#Finding F to degree
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("Enter the temperature: "))
print(f_to_c(f))


#Draw following pattern using recursive Function
# ***
# **
# *
def pattern(m):
    if(m == 0):
        return 1
    print("*" * m)
    pattern(m-1)

pattern(3)
pattern(5)