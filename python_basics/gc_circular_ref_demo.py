import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print("Node {} is being garbage collected".format(self.name))

# We create two nodes that reference each other (cycle)
a = Node("A")
b = Node("B")
a.ref = b
b.ref = a

# We removed main references
del a
del b

print("Collecting garbage...")
gc.collect()  # Force cycle collection
