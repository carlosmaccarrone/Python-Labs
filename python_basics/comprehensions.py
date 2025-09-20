class ConcreteClass:
    def __init__(self, active, value):
        self.active = active
        self.value = value

    def start(self):
        if self.active:
            return "Message {}".format(self.value)
        return None

# Collection of objects
obj_list = [
    ConcreteClass(True, 1),
    ConcreteClass(True, 2),
    ConcreteClass(False, 3),
    ConcreteClass(True, 4),
    ConcreteClass(False, 5),
    ConcreteClass(True, 2)  # Duplicate to display set
]

print("=== Comprehensions ===\n")

#1. List comprehension: all active object messages
list_comp = [obj.start() for obj in obj_list if obj.active]
print("List comprehension:", list_comp)

# 2. Set comprehension: unique values ​​of active objects
set_comp = {obj.value for obj in obj_list if obj.active}
print("Set comprehension:", set_comp)

#3. Dictionary comprehension: value -> message
dict_comp = {obj.value: obj.start() for obj in obj_list if obj.active}
print("Dict comprehension:", dict_comp)

# 4. Generator comprehension: we generate messages one by one (lazy)
gen_comp = (obj.start() for obj in obj_list if obj.active)
print("Generator comprehension (converted to display list):", list(gen_comp))
