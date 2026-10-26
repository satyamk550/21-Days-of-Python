

def get_number(number):
    while True:
        number = input(f"enter number {number}: ")
        try:
            return float(number)
        except :
            print("invalid input. Please enter a valid number.")
number1 = get_number(1)
number2 = get_number(2)
operation = input("enter an operation (+, -, *, /, **, %): ")
if operation == "+":
    result = (number1 + number2)
elif operation == "-":
    result = (number1 - number2)
elif operation == "*":
    result =(number1 * number2)
elif operation =="/":
    if number2 != 0: 
        result = (number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
        result = None    
elif operation =="**":
    result =  (number1 ** number2)
elif operation =="%" :
    result =  (number1 % number2)
print("Result:", result)