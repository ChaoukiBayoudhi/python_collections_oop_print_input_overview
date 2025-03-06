# Example 1: Divide by Zero error handling
print("Example 1: Divide by Zero")
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")  # This line won't be executed
except ZeroDivisionError as zde:
    print(f"Error: Division by zero is not allowed! ({zde})")
finally:
    print("First example completed\n")

# Example 2: Index Out of Range error handling
print("Example 2: Index Out of Range")
try:
    my_list = [1, 2, 3, 4, 5]
    index = 10
    value = my_list[index]
    print(f"Value at index {index}: {value}")  # This line won't be executed
except IndexError as ie:
    print(f"Error: Index {index} is out of range! ({ie})")
finally:
    print("Second example completed")
    
