import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.2f} seconds to execute.")
        return result
    return wrapper

# Example of usage:
@timer
def example_function():
    # Your code here
    time.sleep(2)
    print("Function executed.")

# Call the decorated function
example_function()
