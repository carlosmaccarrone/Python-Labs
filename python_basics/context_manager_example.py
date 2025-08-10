import time

class Timer:
    """
    Context manager to measure the execution time of a code block.
    
    Usage:
        with Timer("My Task"):
            # some code here
            do_something()
    """

    def __init__(self, name="Block"):
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self  # optionally return self if needed inside the block

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        elapsed = end - self.start
        print(f"{self.name} executed in {elapsed:.4f} seconds")

# Example usage
if __name__ == "__main__":
    with Timer("Sleep for a bit"):
        time.sleep(2)