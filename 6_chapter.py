      #If...Else(remove elif)  & if elif else ladder

a = int(input("Enter your age: "))

#If statement 1
if(a % 2 == 0):
    print("a is even number")
 #End of If statement 1   

#if statement 2 & both work independently
if(a>=18):
    print("You are above the age of consent") 
    #some space is given after if() block is to show we are in that block now
elif(a<0): 
    print("Invalid Age")    
elif(a==0):
    print("Age cant be zero")        
else:
    print("You are below the age of consent")
#End of If statement 2

print("End of programm")  
#If can be seprate but else cant and even elif not


# Make a fraud Comment detection 
p1 = "Make lots of money"
p2 = "Buy now"
p3 = "Subcribe this"
p4 = "Click me!"
message = input("Enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Fraud message")
else:
    print("This is not spam") 


# Cheak whether your name is in list or not program
l = ["Pallavi", "Om", "Sanika", "Vaibhav", "Shwet"]
name = input("Enter you name: ")
if(name in l):
    print("Your name is in list")
else:
    print("Your name is not in list")  