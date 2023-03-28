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







