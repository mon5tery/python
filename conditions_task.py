number1 = input("Give me a number: ")
number2 = input("Give me another number: ")
if number1.isnumeric() and number2.isnumeric():
	operation = input("Choose an operation (+, -, /,*)")

	if operation == "+":
		print((int(number1) + int(number2)))
	elif operation == "-":
		print((int(number1) - int(number2)))
	elif operation == "/":
		print((int(number1) / int(number2)))
	elif operation == "*":
		print((int(number1) * int(number2)))
	else:
		print("invalid input")
else:
	print("One of the variables is not a number: ")
#number2 = input("Give me another number: ")
	#if number1 = int(number1):
		#print(number1)
	#else:
		#print("invalid")
#operation = input("Choose one (+, -, /,*): ")
#print()
#print()
	#if number1 = int(number1):
		#print
