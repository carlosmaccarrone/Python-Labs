# Demonstrates the issue with mutable default arguments in Python

def add_task_bad(task_list=[]):
    """
    Adds a task to the default list.
    Warning: Using a mutable default argument can lead to unexpected behavior,
    because the same list is shared across all calls.
    """
    task_list.append("New Task")
    return task_list

def add_task(task_list=None):
    """
    Safe version: initializes a new list if none is provided.
    This prevents data from leaking between function calls.
    """
    if task_list is None:
        task_list = []
    task_list.append("New Task")
    return task_list

# -----------------------
# Examples
# -----------------------
print("Using safe version:")
print(add_task())  # ['New Task']
print(add_task())  # ['New Task'] - fresh list every call
print(add_task(["Custom Task"]))  # ['Custom Task', 'New Task']

print("\nUsing unsafe version:")
print(add_task_bad())  # ['New Task']
print(add_task_bad())  # ['New Task', 'New Task'] - list shared!
print(add_task_bad())  # ['New Task', 'New Task', 'New Task']