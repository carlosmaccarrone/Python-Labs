
## STRING SLICING
##################
print("STRING SLICING")
text_string = "Hello world! how you doing?"
print("My text: {}".format(text_string))

# Word extract
word = text_string[:5]
print(word)

# Reversed text
reversed_text = text_string[::-1]  
print(reversed_text)

# Character skipping (every two letter)
skip_letters = text_string[::2]
print(skip_letters)

# Get the last 6 letters
last_six = text_string[-6:]
print(last_six)

## LIST SLICING
################
print("\nLIST SLICING")
numbers = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]
print("My list: {}".format(numbers))

# First five elements
first_five = numbers[:5]
print(first_five)

# Last three elements
last_three = numbers[-3:]
print(last_three)

# Reversed list
reversed_list = numbers[::-1]
print(reversed_list)

# Get even position elements
even_positions = numbers[::2]
print(even_positions)

# Get sublist from 3th to 7th element
middle_slice = numbers[2:7]
print(middle_slice)

