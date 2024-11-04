# A = L * W

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
print("The area of the rectangle is:", area)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")