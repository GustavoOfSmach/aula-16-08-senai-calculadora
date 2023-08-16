__version__ = "1.0"
__author__ = "GustavoOfSmach"
__license__ = "Unlicense"

number1 = int(input("Coloque o primeiro número: "))
number2 = int(input("Coloque o segundo número: "))
operation = input("Insira a operação matemática (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2

print(f"O resultado da operação foi que {number1} {operation} {number2} é {result}.")
