
"""
Simple example demonstrating the use of threading.BoundedSemaphore in Python.

This script creates multiple threads that try to access a limited resource
protected by a BoundedSemaphore, which allows only a fixed number of concurrent accesses.

Usage:
    Run the script and observe how threads acquire and release the semaphore,
    ensuring no more than the maximum allowed threads run simultaneously.

Author: ChatGPT
"""

import threading
import time

# Create a bounded semaphore with a limit of 3 concurrent accesses
bounded_semaphore = threading.BoundedSemaphore(value=3)

def worker(thread_id):
    print(f"Thread {thread_id} waiting to acquire semaphore...")
    bounded_semaphore.acquire()
    try:
        print(f"Thread {thread_id} has acquired the semaphore.")
        time.sleep(2)  # Simulate work being done
    finally:
        print(f"Thread {thread_id} releasing semaphore.")
        bounded_semaphore.release()

def main():
    threads = []
    for i in range(1, 8):  # 7 threads trying to run
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads have finished execution.")

if __name__ == "__main__":
    main()
    