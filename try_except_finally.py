# Simple example: Basic try-except structure
print("Simple Example: String to Integer conversion")
try:
    # Attempt to convert a string containing letters to integer
    text = "hello"
    number = int(text)    # This will cause a ValueError
    print(f"Converted number: {number}")
except ValueError:
    print("Error: Cannot convert text containing letters to a number!")

print("Simple example completed\n")



# Example 1: Demonstrate handling of ZeroDivisionError
print("Example 1: Divide by Zero")
try:
    # Attempt to perform division by zero
    numerator = 10
    denominator = 0    # This will cause a ZeroDivisionError
    result = numerator / denominator
    print(f"Result: {result}")  # This line won't be executed due to the error
except ZeroDivisionError as zde:
    # Handle the specific case of division by zero
    # 'zde' contains the actual error message
    print(f"Error: Division by zero is not allowed! ({zde})")
finally:
    # This block always executes, whether there was an error or not
    # Useful for cleanup operations
    print("First example completed\n")

# Example 2: Demonstrate handling of IndexError
print("Example 2: Index Out of Range")
try:
    # Create a list with 5 elements (indices 0-4)
    my_list = [1, 2, 3, 4, 5]
    index = 10    # This index is beyond the list's bounds
    value = my_list[index]    # This will cause an IndexError
    print(f"Value at index {index}: {value}")  # This line won't be executed due to the error
except IndexError as ie:
    # Handle the specific case of invalid list index
    # 'ie' contains the actual error message
    print(f"Error: Index {index} is out of range! ({ie})")
finally:
    # This block always executes after try/except blocks
    print("Second example completed")
    
