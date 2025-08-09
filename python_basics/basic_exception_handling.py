

try:
    user_input = int(input("Enter a number: "))
    result = 10 / user_input
except ValueError:
    print("Error: You must enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution finished.")

