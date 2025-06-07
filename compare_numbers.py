# Take input from user and convert to integer
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compare and print result
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
