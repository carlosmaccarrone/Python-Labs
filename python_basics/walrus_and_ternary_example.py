

def process_input():
    while (user_input := input("Enter a number (or 'exit' to quit): ")) != "exit":
        # Ternary condition to validate and process
        result = int(user_input) * 2 if user_input.isdigit() else "Invalid input"
        print(f"Result: {result}")

    print("Goodbye!")

if __name__ == "__main__":
    process_input()

