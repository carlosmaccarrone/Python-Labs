class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # This helps to print the object in a readable way
        return f"User(name='{self.name}')"


# Create a list of User objects
users = [
    User("Charlie"),
    User("Alice"),
    User("Bob"),
    User("David")
]

print("Before sorting:", users)

# Define a function that returns the property 'name'
def get_name(user):
    return user.name

# Sort the list of users by their name
users.sort(key=get_name)
print("After sorting:", users)

# You can also sort the object list without declaring a function by using lambda expressions, like this:
users = [
    User("Charlie"),
    User("Alice"),
    User("Bob"),
    User("David")
]

# Sort the list of users by their name
users.sort(key=lambda user: user.name)
print("After sorting:", users)