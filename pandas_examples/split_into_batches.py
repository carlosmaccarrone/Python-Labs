
# This function is a classic for handling large data in chunks without breaking up RAM.

def split_into_batches(iterable, batch_size):
    length = len(iterable)
    for ndx in range(0, length, batch_size):
        yield iterable[ndx : min(ndx + batch_size, length)]

if __name__ == "__main__":
    # Suppose we have 23 records (can be IDs, objects, etc.)
    data = list(range(1, 24))

    print("Complete dataset:", data)

    # We want to process in batches of 5
    for i, batch in enumerate(split_into_batches(data, 5), start=1):
        print(f"Batch {i}: {batch}")

