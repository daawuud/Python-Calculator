# Calculador
from art import logo

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    opration_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[opration_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {opration_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()  
      
      
  # opration_symbol = input("Pick another operation: ")
  # num3 = int(input("What's the next number?: "))
  # calculation_function = operations[opration_symbol]
  # second_answer = calculation_function(first_answer, num3)
  # print(f"{first_answer} {opration_symbol} {num3} = {second_answer}")
  
  # operation_symbol = input("Pick another operation: ")
  # num4 = int(input("What's the next number?: "))
  # calculation_function = operations[operation_symbol]
  # third_answer = calculation_function(second_answer, num4)
  # print(f"{second_answer} {operation_symbol} {num4} = {third_answer}")
  
