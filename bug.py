def function_with_uncommon_error(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Handle the error explicitly
    except TypeError:
        print("Error: Invalid operand types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# Example usage demonstrating the error handling
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero, None
print(function_with_uncommon_error(10, "a"))  # Output: Error: Invalid operand types, None
print(function_with_uncommon_error(10, [1,2])) # Output: Error: unsupported operand type(s) for /: 'int' and 'list', None