from project.Calculator import Calculator

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