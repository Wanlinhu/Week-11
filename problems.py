
name = input("What is your name? ")
age = input("What is your age? ")

print("Name:", name, type(name))
print("Age:", age, type(age))

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")


num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal.")

color = input("What is your favorite color? ")
print("Your favorite color is:", color)
print("Type of favorite color:", type(color))

float_input = input("Enter a floating-point number: ")
float_number = float(float_input)

print("You entered:", float_number)
print("Data type:", type(float_number))


name = input("Enter your full name: ")
name_length = len(name)

print("Length of your name:", name_length)
print("Data type:", type(name_length))


