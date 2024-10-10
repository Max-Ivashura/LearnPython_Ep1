def calculator():
    operator = input("Enter an operator (+ - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2st number: "))

    if operator == '+':
        print(round(num1 + num2, 3))
    elif operator == '-':
        print(round(num1 - num2, 3))
    elif operator == '*':
        print(round(num1 * num2, 3))
    elif operator == '/':
        print(round(num1 / num2, 3))
    else:
        print("Error! Operator not found!")
        return 0


calculator()
