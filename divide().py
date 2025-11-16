def divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return None
	
# TAKE INPUT FROM USER
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
# CALL THE FUNCTION AND PRINT THE RESULT
result = divide(num1, num2)
if result is None:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")
	

