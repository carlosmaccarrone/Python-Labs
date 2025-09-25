"""
Didactic example of a Closure in Python 3
-----------------------------------------
A *closure* is a function that remembers the values of variables
from the scope where it was created, even if that scope no longer exists.
"""

def create_multiplier(factor):
    """
    Outer function that receives a 'factor'
    and returns an inner function (closure)
    that will keep using that value later.
    """
    def multiply(number):
        return number * factor  # 'factor' is "closed over" in the scope
    return multiply


# We create two different functions from the same generator
double = create_multiplier(2)
triple = create_multiplier(3)

# Testing the closures
print(double(5))   # 10
print(triple(5))   # 15

"""
Closures encapsulate logic (the element is trapped in the inner function).

They are useful for creating custom functions without the need for classes.

They have practical applications in decorators, callbacks, and functional programming.
"""