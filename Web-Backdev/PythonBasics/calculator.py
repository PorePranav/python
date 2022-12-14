num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))

op = input("Enter operator ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("No valid operator entered")