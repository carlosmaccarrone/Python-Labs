import time

def timer_decorator(func):
    """
    Decorator that measures and prints the execution time of the decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def example_function(n):
    """
    Example function that sums numbers from 0 to n-1 with a small delay.
    """
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.01)  # simulate work
    return total

if __name__ == "__main__":
    result = example_function(10)
    print(f"Result: {result}")