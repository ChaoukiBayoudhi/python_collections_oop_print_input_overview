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

# Example 3: Demonstrate handling of KeyError
print("Example 3: Key Not Found")
try:
    # Create a dictionary with some key-value pairs
    my_dict = {"name": "Alice", "age": 30, "city": "Wonderland"}
    key = "country"    # This key is not present in the dictionary
    value = my_dict[key]    # This will cause a KeyError
    print(f"Value for key '{key}': {value}")  # This line won't be executed due to the error
except KeyError as ke:
    # Handle the specific case of missing key in dictionary
    # 'ke' contains the actual error message
    print(f"Error: Key '{key}' not found in dictionary! ({ke})")


# Example 4: Demonstrate handling of TypeError
print("Example 4: Type Mismatch")
try:
    # Attempt to add a string to an integer
    number = 42
    text = "Hello"
    result = number + text    # This will cause a TypeError
    print(f"Result: {result}")  # This line won't be executed due to the error
except TypeError as te:
    # Handle the specific case of type mismatch
    # 'te' contains the actual error message
    print(f"Error: Cannot add integer and string! ({te})") 

# Example 5: Demonstrate handling of FileNotFoundError
print("Example 5: File Not Found")
try:
    # Attempt to open a non-existent file for reading
    file_path = "missing_file.txt"
    with open(file_path, "r") as file:
        content = file.read()
        print(f"File content: {content}")
except FileNotFoundError as fnfe:
    # Handle the specific case of missing file
    # 'fnfe' contains the actual error message
    print(f"Error: File '{file_path}' not found! ({fnfe})")

# Example 6: Demonstrate handling of multiple exceptions
print("Example 6: Multiple Exceptions")
try:
    # Attempt to perform an operation that raises multiple exceptions
    num1 = 10
    num2 = 0
    result = num1 / num2    # This will cause a ZeroDivisionError
    print(f"Result: {result}")  # This line won't be executed due to the error
except ZeroDivisionError as zde:
    # Handle the specific case of division by zero
    print(f"Error: Division by zero is not allowed! ({zde})")
except TypeError as te:
    # Handle the specific case of type mismatch
    print(f"Error: Cannot add integer and string! ({te})")
finally:
    # This block always executes after try/except blocks
    print("All examples completed")

# Example 7: Demonstrate handling of generic exceptions
print("Example 7: Generic Exception")
try:
    # Attempt to perform an operation that raises an exception
    num1 = 10
    num2 = 0
    result = num1 / num2    # This will cause a ZeroDivisionError
    print(f"Result: {result}")  # This line won't be executed due to the error
except Exception as e:
    # Handle any exception that occurs
    # 'e' contains the actual error message
    print(f"Error: An exception occurred! ({e})")

# Example 8: Demonstrate handling of exceptions without error details
print("Example 8: No Error Details")
try:
    # Attempt to perform an operation that raises an exception
    num1 = 10
    num2 = 0
    result = num1 / num2    # This will cause a ZeroDivisionError
    print(f"Result: {result}")  # This line won't be executed due to the error
except ZeroDivisionError:
    # Handle the specific case of division by zero without error details
    print("Error: Division by zero is not allowed!")

# Example 9: Demonstrate handling of exceptions without specifying the error type
print("Example 9: No Error Type")
try:
    # Attempt to perform an operation that raises an exception
    num1 = 10
    num2 = 0
    result = num1 / num2    # This will cause a ZeroDivisionError
    print(f"Result: {result}")  # This line won't be executed due to the error
except:
    # Handle any exception that occurs without specifying the error type
    print("Error: An exception occurred!")

# Define a custom exception class
class CustomError(Exception):
    pass

# Example 10: Demonstrate handling of custom exceptions
print("Example 10: Custom Exception")
try:
    # Raise a custom exception with a specific message
    raise CustomError("This is a custom error message")
except CustomError as ce:
    # Handle the custom exception
    # 'ce' contains the actual error message
    print(f"Custom Error: {ce}")
    
# Define advanced custom exception classes
class CustomValueError(ValueError):
    def __init__(self, value):
        super().__init__(f"Invalid value: {value}")
    def __str__(self):
        return f"Custom ValueError: {self.args[0]}"
    
class CustomTypeError(TypeError):
    def __init__(self, value):
        super().__init__(f"Invalid type: {type(value).__name__}")
    def __str__(self):
        return f"Custom TypeError: {self.args[0]}"
    
# Example 11: Demonstrate handling of advanced custom exceptions
print("Example 11: Advanced Custom Exceptions")
try:
    # Raise a custom ValueError with a specific value
    raise CustomValueError("abc")
except CustomValueError as cve:
    # Handle the custom ValueError
    print(cve)

try:
    # Raise a custom TypeError with a specific value
    raise CustomTypeError(42)
except CustomTypeError as cte:
    # Handle the custom TypeError
    print(cte)

# Example 12: Demonstrate handling of exceptions in a loop
print("Example 12: Exception Handling in a Loop")
# Define a list of values to process
values = [10, 0, "hello", 20, 5, 0, "world"]
# Process each value in the list
for value in values:
    try:
        # Attempt to perform an operation that raises an exception
        result = 100 / value    # This may cause a ZeroDivisionError or TypeError
        print(f"Result: {result}")  # This line won't be executed if an error occurs
    except ZeroDivisionError:
        # Handle the specific case of division by zero
        print("Error: Division by zero is not allowed!")
    except TypeError:
        # Handle the specific case of type mismatch
        print("Error: Cannot divide by a non-numeric value!")
    except Exception as e:
        # Handle any other exception that occurs
        print(f"Error: An exception occurred! ({e})")
print("All examples completed")

# Example 13: Demonstrate handling of exceptions in a function
print("Example 13: Exception Handling in a Function")
# Define a function that raises an exception
def divide_numbers(numerator, denominator):
    try:
        # Attempt to perform division
        result = numerator / denominator    # This may cause a ZeroDivisionError
        return result
    except ZeroDivisionError:
        # Handle the specific case of division by zero
        return
    except Exception as e:
        # Handle any other exception that occurs
        return f"Error: An exception occurred! ({e})"
# Test the function with different inputs
print(divide_numbers(10, 2))    # Should print 5.0
print(divide_numbers(42, 0))    # Should print None
print(divide_numbers("hello", 5))    # Should print an error message

# Example 14: Demonstrate handling of exceptions in a class
print("Example 14: Exception Handling in a Class")
# Define a class that raises an exception
class Calculator:
    def divide_numbers(self, numerator, denominator):
        try:
            # Attempt to perform division
            result = numerator / denominator    # This may cause a ZeroDivisionError
            return result
        except ZeroDivisionError:
            # Handle the specific case of division by zero
            return
        except Exception as e:
            # Handle any other exception that occurs
            return f"Error: An exception occurred! ({e})"
# Create an instance of the class
calc = Calculator()
# Test the class method with different inputs
print(calc.divide_numbers(10, 2))    # Should print 5.0
print(calc.divide_numbers(42, 0))    # Should print None
print(calc.divide_numbers("hello", 5))    # Should print an error message

#propogation of exceptions
def divide_numbers(numerator, denominator):
    try:
        # Attempt to perform division
        result = numerator / denominator    # This may cause a ZeroDivisionError
        return result
    except ZeroDivisionError as zde:
        # Handle the specific case of division by zero
        raise ValueError("Cannot divide by zero!") from zde
    except Exception as e:
        # Handle any other exception that occurs
        raise Exception("An error occurred!") from e
try:
    # Attempt to divide by zero
    divide_numbers(42, 0)
except ValueError as ve:
    # Handle the specific case of division by zero
    print(f"ValueError: {ve}")
except Exception as e:
    # Handle any other exception that occurs
    print(f"Exception: {e}")

#full real word example that include the use of all about exceptions in a single example
# Define a custom exception class for invalid input
class InvalidInputError(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid input: {value}")
    def __str__(self):
        return f"InvalidInputError: {self.args[0]}"
# Define a function to calculate the next day of the week
def next_day(date):
    try:
        # Calculate the next day of the week
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        next_day_name = days[(days.index(date[0]) + 1) % 7]
        next_year = date[3]  # Initialize next year as the current year
        # Check if the current date is December 31st and update accordingly
        if date[2] == 12 and date[1] == 31:
            next_month = 1  # Move to January
            next_year = date[3] + 1  # Increment the year
            next_day_of_month = 1  # Reset the day of the month to 1
        # Check for specific month and day combinations that require a month change
        elif date[2] == 2 and date[1] == 28 and date[3] % 4 == 0 and (date[3] % 100 != 0 or date[3] % 400 == 0) or (date[2] in (4, 6, 9, 11) and date[1] == 30) or (date[2] in (1, 3, 5, 7, 8, 10) and date[1] == 31) or (date[2] == 2 and date[1] == 29):
            next_month = date[2] + 1  # Move to the next month
            next_day_of_month = 1  # Reset the day of the month to 1
        else:
            next_month = date[2]  # Keep the current month
            next_day_of_month = date[1] + 1  # Increment the day of the month
        return (next_day_name, next_day_of_month, next_month, next_year)
    except ValueError as ve:
        # Handle the specific case of invalid input
        raise InvalidInputError(date) from ve
    except Exception as e:
        # Handle any other exception that occurs
        raise Exception("An error occurred!") from e
# Test the function with different inputs
try:
    # Test with valid input
    print(next_day(("Monday", 28, 2, 2000)))  # Should print ('Tuesday', 29, 2, 2000)
    # Test with invalid input
    print(next_day(("Monday", 31, 4, 2021)))  # Should raise an InvalidInputError
except InvalidInputError as iie:
    # Handle the specific case of invalid input
    print(iie)
except Exception as e:
    # Handle any other exception that occurs
    print(f"Exception: {e}")

# Real-world example to demonstrate the importance of the finally block
#the finally bloc with traitment like closing a file or a database connection, cleaning up resources and releasing locks
# Define a function to read the contents of a file and store it into database
def read_file_and_store_data(file_path):
    file = None
    try:
        # Open the file for reading
        file = open(file_path, "r")
        # Read the contents of the file
        data = file.read()
        # Store the data into the database (not implemented)
        import psycopg2

        def connect_to_database(host, database, user, password):
            try:
                # Establish a connection to the PostgreSQL database
                connection = psycopg2.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password
                )
                return connection
            except psycopg2.OperationalError as oe:
                print(f"Error: Unable to connect to the database! ({oe})")
                return None

        def store_data_into_database(connection, data):
            try:
                # Create a cursor object to execute SQL queries
                cursor = connection.cursor()
                # SQL query to insert data into a table (replace with actual table name)
                query = "INSERT INTO my_table (data) VALUES (%s)"
                # Execute the query with the data
                cursor.execute(query, (data,))
                # Commit the changes
                connection.commit()
                print("Data stored successfully into the database!")
            except psycopg2.Error as pe:
                print(f"Error: Unable to store data into the database! ({pe})")

        # Connect to the PostgreSQL database
        connection = connect_to_database("localhost", "my_database", "my_user", "my_password")
        if connection:
            # Store the data into the database
            store_data_into_database(connection, data)
            # Close the database connection
            connection.close()
        print(f"Data stored successfully: {data}")
    except FileNotFoundError as fnfe:
        # Handle the specific case of missing file
        print(f"Error: File '{file_path}' not found! ({fnfe})")
    except Exception as e:
        # Handle any other exception that occurs
        print(f"Error: An exception occurred! ({e})")
    finally:
        # This block always executes after try/except blocks
        # Useful for cleanup operations
        if file:
            file.close()
            print("Cleanup: Closing file")
            del file
            print("Cleanup: File object deleted")
        print("Cleanup: All resources released")
