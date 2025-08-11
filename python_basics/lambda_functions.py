

numbers = [1, 2, 3, 4, 5, 6]

# map >>> square each number
squares = list(map(lambda x: x**2, numbers))

# filter >>> select only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Squares:", squares)
print("Evens:", evens)


squaresAgain = lambda x: x**2
mapped_squares = [ squaresAgain(num) for num in numbers ]
print("SquaresAgain:", mapped_squares)
