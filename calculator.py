
print("Welcome to the Super Simple Calculator!")
print("This calculator only works with two numbers at a time.")
print("Operations available: + (addition), - (subtraction), * (multiplication) and / (division)")
print("------------------------------------------------------")

# First, we ask the user for the first number.
try:
    num1_text = input("Please enter your first number: ")
    num1 = float(num1_text)
except ValueError:
    # If the user enters something that is not a number, we stop.
    print("Oops! That wasn't a valid number. Please restart.")
    exit()

# Next, we ask for the operation.
operation = input("Enter the operation (+, -, *, /,): ")

# Finally, we ask for the second number.
try:
    num2_text = input("Please enter your second number: ")
    num2 = float(num2_text)
except ValueError:
    print("Oops! That wasn't a valid number. Please restart.")
    exit()

# Now we check which operation the user chose.
if operation == '+':
    # If it's addition, we add the numbers.
    result = num1 + num2
    print(f"Adding {num1} and {num2}...")
    print(f"The result is: {result}")

elif operation == '-':
    # If it's subtraction, we subtract the numbers.
    result = num1 - num2
    print(f"Subtracting {num2} from {num1}...")
    print(f"The result is: {result}")

elif operation == '*':
    #if it's multiplication, we multiply the numbers.
    result = num1 * num2
    print(f"Multiplying {num1} and {num2}...")
    print(f"The result is: {result}")

elif operation == '/':
    #if it's division, we divide the numbers.
    result = num1/num2
    print("dividing {num1} by {num2}...")
    print(f"The result is: {result}")

else:
    # If the user didn't enter '+', '-', '*', '/' we tell them it's an error.
    print("Sorry, I don't know how to do that operation yet!")
    print("I can only do '+', '-', '*' '/'.")

print("Thank you for using the calculator!")
