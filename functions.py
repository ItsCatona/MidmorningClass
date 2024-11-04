#Built-in Functions

y = max(34, 556, 67, 23, 57)
print(y)

x = min(45, 67, 87, 23, 67, 12, 10)
print(x)

z = pow(4, 7) #4 power raised 7
print("answer is", z)

#User-defined functions
def greeting():
    print("Hello there")

greeting() #Calling Function

def multiply():
    a = 12
    b = 10
    print(a * b)

multiply()

#Parameters/Variable and Argument/Value
def add(x , y):
    print(x + y)

add(4,6)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)

employee("Mark Hope",54,"CEO","Married")
employee("Jane Anne",24,"HR","Single")
employee("Phil Jones",34,"Clerk","Single")
employee("Mary Jane",26,"Receptionist","Married")

