num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

print("\nPlease select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

op = int(input("\nEnter your choice (1-4): "))

def addition():
    result = num1 + num2
    return int(result)

def substraction():
    result = num1 - num2
    return int(result)

def multiplier():
    result = num1 * num2
    return int(result)

def division():
    result = num1 / num2 if num2 != 0 else "division by zero is not allowed"
    return (result)

if op == 1:
    print(f"\nThe result of multiplication is: {addition()}")

if op == 2:
    print(f"\nThe result of multiplication is: {substraction()}")

if op == 3:
    print(f"\nThe result of multiplication is: {multiplier()}")

if op == 4:
    print(f"\nThe result of multiplication is: {division()}")

if op >=5:
    print("\nGood try)")