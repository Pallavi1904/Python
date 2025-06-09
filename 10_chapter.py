# Object Oriented Programming

class Employee:  #class 
    language = "python"  #class attribute
    salary = 1200000

emp1 = Employee() #object
emp1.name = "Hemant"  
print(emp1.name, emp1.language, emp1.salary)


#name is object attribute and lang and salary are class attribute as they directly belongs to class
emp2 = Employee()
emp2.name = "Radha"  # object attribute
print(emp2.name, emp2.language, emp2.salary)



#Instance attribute take Preference over class attribute during assignment and retrival
emp3 = Employee()
emp3.name = "ram"
emp3.language = "Java" #overlapped
print(emp3.name, emp3.language, emp3.salary)




# Self parameter
class Employee2:   
    lang = "cpp"  
    sal = 100000
    def getinfo(Self): #self used
        print(f"The language is {Self.lang} and salary is {Self.sal}")


# Whether self is use or not in function we have to give it to function    
    def sweet(self):
        print("Mangoo is sweet")


# Static methods
    @staticmethod
    def sweet2():
        print("Apple is more switer")        

emp = Employee2()
emp.sal = 13000 #instance attribute
emp.getinfo()

emp.sweet()

emp.sweet2()

#  _ _init_ _() Constructor
class Programming:
    def __init__(self, name, salary): # Dunder method which call itself
        self.name = name
        self.salary = salary
        print(name, salary)
        print("hmmmmmmmmmmmmmmmmmmmmmmm")

h = Programming("Pallavi", 1300000) #name00


# Write a programm in class with function to print square squareroot and cube
class Operations:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"Square is: {self.n * self.n}")
    
    def squareRoot(self):
        print(f"Square root is: {self.n**(1/2)}")
    
    def cube(self):
        print(f"Cube is: {self.n * self.n * self.n}")
    
opp1 = Operations(4)
opp1.square()
opp1.squareRoot()
opp1.cube()


# To understand methods and constructor in python
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")
    def status(self):
        print(f"Train no {self.trainNo} is running")
    def getFar(self, fro, to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(22, 5555)}")

t = Train(19)
t.book("Pune", "Mumbai")
t.status()
t.getFar("Pune", "Mumbai")

