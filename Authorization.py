class UnauthorizedError(Exception):
    pass

def authorize(expected_username, expected_password):
    def decorator(func):
        def wrapper(username, password, *args, **kwargs):
            if username == expected_username and password == expected_password:
                return func(*args, **kwargs)
            else:
                raise UnauthorizedError("Unauthorized: Invalid credentials")

        return wrapper

    return decorator

# Example of usage:
@authorize(expected_username="admin", expected_password="secret123")
def sensitive_operation():
    print("Sensitive operation successful!")

# Test cases:
try:
    sensitive_operation("admin", "wrong_password")
except UnauthorizedError as e:
    print(e)

try:
    sensitive_operation("user", "secret123")
except UnauthorizedError as e:
    print(e)

try:
    sensitive_operation("admin", "secret123")
except UnauthorizedError as e:
    print(e)
else:
    # This block will execute if the authorization is successful
    sensitive_operation("admin", "secret123")
