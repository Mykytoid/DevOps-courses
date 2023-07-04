
def input_first_num():
    try:
        num1 = float(input("Please enter the first number: "))
        return num1
    except:
        input_first_num()


def input_second_num():
    try:
        num2 = float(input("Please enter the second number: "))
        return num2
    except:
        input_second_num()

def select(num1, num2):
    print("\nPlease select an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    op = int(input("\nEnter your choice (1-4): "))
    operation(op, num1, num2)

# select()
def addition(num1, num2):
    result = num1 + num2
    return result

def subtraction(num1, num2):
    result = num1 - num2
    return result

def multiplication(num1, num2):
    result = num1 * num2
    return result

def division(num1, num2):
    result = num1 / num2 if num2 != 0 else "division by zero is not allowed"
    return result

def operation(op, num1, num2):

    if op == 1:
        result = addition(num1, num2)
        print(f"\nThe result of addition is: {result}")

    elif op == 2:
        result = subtraction(num1, num2)
        print(f"\nThe result of subtraction is: {result}")

    elif op == 3:
        result = multiplication(num1, num2)
        print(f"\nThe result of multiplication is: {result}")

    elif op == 4:
        result = division(num1, num2)
        print(f"\nThe result of division is: {result}")

    else:
        print("\nInvalid choice! Please select a number from 1 to 4.")
        select()

    reinit()

def reinit():
    answer = input("Do you want new calculation? (Y/N): ");

    if answer.lower() == "y":
        main();
    elif answer.lower() == "n":
        print("\nGoodbye!")
    else:
        print("\nInvalid input! Please enter Y or N.")
        reinit()

def main():
    num1 = input_first_num()
    num2 = input_second_num()
    select(num1, num2)

main()
