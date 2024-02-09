def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print(f"Cache hit for {func.__name__} with arguments {key}")
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            print(f"Cache miss for {func.__name__} with arguments {key}")
            return result

    return wrapper

# Example of usage:
@memoize
def add(x, y):
    print(f"Calculating sum of {x} and {y}")
    return x + y

# Call the decorated function
print(add(2, 3))  # Will compute and print, as it's the first time
print(add(2, 3))  # Will use cached result and print "Cache hit"
print(add(4, 5))  # Will compute and print, as it's a different set of arguments
print(add(4, 5))  # Will use cached result and print "Cache hit"
