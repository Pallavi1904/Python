class Employee: #Base class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    company = "ITC"

    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")


class Programmer (Employee): # Derived class
    def __init__(self, name, salary, language): 
        self.language = language
        super().__init__(name, salary)

    company = "ITC Infotech"
    
    def showLanguage(self):
        print(f"The name is {self.name} and language is {self.language}")


a = Employee("Pallavi", 4500000)
b = Programmer("Pallavi", 4500000,"Python")

b.show()
b.showLanguage()
print(a.company, b.company)


# Multilevel Inheritance
class Employee2:
    a = 1
class Programmer2(Employee2):
    b = 2
class Manager(Programmer2):
    c = 3

m = Employee2()
print(m.a)

n = Programmer2()
print(n.a)
print(n.b)

o = Manager()
print(o.a)
print(o.b)
print(o.c)


# Class Methods
class ClassMethod:
    a = 1
    @classmethod #Syntax to make class attribute dafult with cls 
    def show3(cls):
        print(f"The class attribute is {cls.a}")

o = ClassMethod()
o.a = 45
o.show3() #not shows 45 but making it classmethod it will show class attribute


# Property Decorators
class Property:
    @property #It provides variable as internal function even after declaring it at object
    def show4(self):
        return self.name

    @show4.setter
    def show4(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
m = Property()
m.name = "Pallavi Akolkar"
print(m.name)


# Operator Overloading
class Number:
    def __init__(self, n):
        self.n = n
    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
print(n + m)






