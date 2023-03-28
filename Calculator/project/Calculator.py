class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero!"

    @staticmethod
    def calculate(a, command, b):
        if command == "+":
            result = Calculator.add(a, b)
            return result
        elif command == "-":
            result = Calculator.subtract(a, b)
            return result
        elif command == "*":
            result = Calculator.multiply(a, b)
            return result
        elif command == "/":
            result = Calculator.division(a, b)
            return result
        else:
            return "Unknown operation! Please choose something from the valid ones!"


print("Hello and welcome to the best calculator in the world!")
print("Please insert your function like this: 2 + 2 !!!")
print("The symbols: / - division, * - multiplication, + - addition, - - subtraction.")
calculator = Calculator
while True:
    operation = input().split()
    a = float(operation[0])
    command = str(operation[1])
    b = float(operation[2])
    print(calculator.calculate(a, command, b))





