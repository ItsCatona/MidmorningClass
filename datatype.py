
number = 56 #interger
second = 43.12 #Float
greeting = "Hello there" #string
isPythonInteresting = True #Boolean

#Data Structures- Multiple values stored in a single variable
cars = ["toyota", "nissan", "VW"] #List - Ordered and changeable
fruits = ("banana", "orange", "apple")#Turple - Ordered but unchangeable
countries = {"kenya", "Tunisia", "Namibia"} #Set - unordered and unchangeable
student = {
    "firstnane" : "Moses",
    "age" : 21,
    "course" : "web development",
    "nationality" : "kenyan"
} #Dictionary - key-value pair

print(number)
print(second)
print(isPythonInteresting)
print(cars)
print(fruits)
print(student)
print(countries)
print(student["course"])

#Determining a datatype
print(type(student))
print(type(countries))

#Typecasting - Conveerting one type into another
print(float(number))
print(int(second))
