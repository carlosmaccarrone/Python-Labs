"""
basic_exception_logging.py

A simple example to demonstrate how to capture detailed exception information 
and log it to a file using Python's logging module.

This script shows how to:
- Catch exceptions in a try/except block
- Log the full traceback with timestamp automatically
- Print a friendly error message for the user

Author: Carlos Esteban Maccarrone -cem-
"""

import logging

# Configure logging once at the start of the script
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def example_function():
    print("Hello world\nHow are you?")
    # Raise an example controlled exception
    raise Exception("This is a controlled exception")
    # Other function code would go here...

def main():
    try:
        example_function()
    except Exception as e:
        # Log the full exception traceback with timestamp
        logging.error("Exception occurred", exc_info=True)
        # Print a user-friendly message
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()