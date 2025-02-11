def function_with_improved_error_handling(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: Invalid operand types: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Optionally log the error for debugging or send it to an error monitoring service
        return None
    return result

# Example usage
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero, None
print(function_with_improved_error_handling(10, "a"))  # Output: Error: Invalid operand types: unsupported operand type(s) for /: 'int' and 'str', None