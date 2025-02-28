# This section demonstrates various list operations
l = [4, 11, 3, 8, 11, 33]  # Initialize a list with integers
print(l)  # Print the initial list
l.append(100)  # Append 100 to the end of the list
print(l)  # Print the list after appending
l.insert(2, 200)  # Insert 200 at index 2
print(l)  # Print the list after insertion
l.pop()  # Remove the last element from the list
print(l)  # Print the list after popping
l.pop(1)  # Remove the element at index 1
print(l)  # Print the list after popping
l.remove(8)  # Remove the first occurrence of 8
print(l)  # Print the list after removal
l.append(100)  # Append 100 again
l.insert(2, 100)  # Insert 100 at index 2
l.insert(4, 100)  # Insert 100 at index 4
print(l)  # Print the list after multiple insertions
# l.remove(100)  # Uncomment to remove the first occurrence of 100
print(l)  # Print the list after removal
print(len(l))  # Print the length of the list

# Create a list of even integers between 0 and 100 using different methods
# Method 1: Using a for loop and append
L = []
for i in range(0, 101, 2):
    L.append(i)
print(L)  # Print the list of even numbers

# Method 2: Using list comprehension
L = [2 * i for i in range(51)]
print(L)  # Print the list of even numbers

# Method 3: Using the range function
L = list(range(0, 101, 2))
print(L)  # Print the list of even numbers

# Method 4: Using list comprehension with a condition
L = [i for i in range(101) if i % 2 == 0]
print(L)  # Print the list of even numbers

# Method 5: Using a while loop
i = 0
L = []
while i <= 100:
    L = L + [i]
    i += 2
print(L)  # Print the list of even numbers

# Method 6: Using a predefined list size
L = [0] * 51
for i in range(51):
    L[i] = 2 * i
print(L)  # Print the list of even numbers

# Using the add operation
L = []
for i in range(51):
    L += [2 * i]
print(L)  # Print the list of even numbers

# Using the extend method
L = []
for i in range(51):
    L.extend([2 * i])
print(L)  # Print the list of even numbers

# Using the insert method
L = []
for i in range(51):
    L.insert(i, 2 * i)
print(L)  # Print the list of even numbers

# Demonstrating other list functions
L = [4, 11, 3, 8, 11, 33]  # Initialize a list
print(L)  # Print the list
print(L.count(11))  # Count occurrences of 11
print(L.index(11))  # Find the index of the first occurrence of 11
print(L.index(11, 2))  # Find the index of 11 starting from index 2
L.sort()  # Sort the list in ascending order
L.reverse()  # Reverse the list
print(L)  # Print the reversed list
L.sort(reverse=True)  # Sort the list in descending order
print(L)  # Print the sorted list
L.clear()  # Clear the list
print(L)  # Print the empty list

# Generate a list randomly
from random import randint  # Import randint from random module
L = [randint(0, 100) for i in range(10)]  # Generate a list of 10 random integers
print(L)  # Print the random list
L.sort()  # Sort the list
print(L)  # Print the sorted list

# Generate a list randomly using numpy
import numpy as np  # Import numpy
L = np.random.randint(0, 100, 10)  # Generate a list of 10 random integers using numpy
print(L)  # Print the random list
L.sort()  # Sort the list
print(L)  # Print the sorted list

# Generate a list randomly using other ways
L = [randint(0, 100) for _ in range(10)]  # Generate a list of 10 random integers
print(L)  # Print the random list

# Generate a list of float randomly using numpy
L = np.random.rand(10)  # Generate a list of 10 random floats
print(L)  # Print the random list

# Generate a list of float randomly
L = [randint(0, 100) / 100 for _ in range(10)]  # Generate a list of 10 random floats
print(L)  # Print the random list

# Generate a list of strings randomly using numpy
L = np.random.choice(['a', 'b', 'c'], 10)  # Generate a list of 10 random strings
print(L)  # Print the random list

# Generate a list of strings randomly
L = [chr(randint(97, 99)) for _ in range(10)]  # Generate a list of 10 random strings
print(L)  # Print the random list

# Generate a list of strings of length n randomly
n = 10  # Define the length of the list
L = [chr(randint(97, 99)) for _ in range(n)]  # Generate a list of n random strings
print(L)  # Print the random list

# Generate a list of strings of length n randomly using numpy
n = 10  # Define the length of the list
L = np.random.choice(['a', 'b', 'c'], n)  # Generate a list of n random strings
print(L)  # Print the random list

# Generate a list of strings of length n from all alphabetics randomly using numpy
n = 10  # Define the length of the list
L = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), n)  # Generate a list of n random strings
print(L)  # Print the random list

# Generate a list of strings of length n from all alphabetics randomly
n = 10  # Define the length of the list
L = [chr(randint(97, 122)) for _ in range(n)]  # Generate a list of n random strings
print(L)  # Print the random list

# Generate a list of (strings of (length n)) from all alphabetics randomly using numpy
n = 10  # Define the length of the list
L = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), n)  # Generate a list of n random strings
L = [''.join(L) for _ in range(n)]  # Join the strings to form a list of strings
print(L)  # Print the random list

# Generate a list of (strings of (length n)) from all alphabetics randomly
n = 10  # Define the length of the list
L = [chr(randint(97, 122)) for _ in range(n)]  # Generate a list of n random strings
L = [''.join(L) for _ in range(n)]  # Join the strings to form a list of strings
print(L)  # Print the random list

# Overview of string functions and methods
s = 'hello'  # Define a string
print(s)  # Print the string
print(s[0])  # Print the first character of the string

# Predefined string functions
print(len(s))  # Print the length of the string
print(s.upper())  # Convert the string to uppercase
print(s.lower())  # Convert the string to lowercase
print(s.capitalize())  # Capitalize the first letter of the string
print(s.title())  # Convert the string to title case
print(s.swapcase())  # Swap the case of the string
print(s.isalpha())  # Check if the string contains only alphabetic characters
print(s.isdigit())  # Check if the string contains only digits
print(s.isalnum())  # Check if the string contains only alphanumeric characters
print(s.isspace())  # Check if the string contains only whitespace
print(s.startswith('h'))  # Check if the string starts with 'h'
print(s.endswith('o'))  # Check if the string ends with 'o'
print(s.find('l'))  # Find the first occurrence of 'l'
print(s.rfind('l'))  # Find the last occurrence of 'l'
print(s.count('l'))  # Count the occurrences of 'l'
print(s.replace('l', 'L'))  # Replace 'l' with 'L'
print(s.split('l'))  # Split the string at 'l'
print(s.split('l', 1))  # Split the string at the first occurrence of 'l'
print(s.rsplit('l'))  # Split the string at 'l' from the right
print(s.rsplit('l', 1))  # Split the string at the last occurrence of 'l'
print(s.join(['a', 'b', 'c']))  # Join the list with the string as a separator
print(s.join(['a', 'b', 'c']).split(s))  # Split the joined string at 's'
print(s.join(['a', 'b', 'c']).split(s, 1))  # Split the joined string at the first occurrence of 's'
print(s.join(['a', 'b', 'c']).rsplit(s))  # Split the joined string at 's' from the right
print(s.join(['a', 'b', 'c']).rsplit(s, 1))  # Split the joined string at the last occurrence of 's'
print(s.center(10))  # Center the string in a field of width 10
print(s.ljust(10))  # Left justify the string in a field of width 10
print(s.rjust(10))  # Right justify the string in a field of width 10
print(s.zfill(10))  # Pad the string with zeros to a width of 10
print(s.strip())  # Strip whitespace from both ends of the string
print(s.lstrip())  # Strip whitespace from the left end of the string
print(s.rstrip())  # Strip whitespace from the right end of the string
print(s.strip('o'))  # Strip 'o' from both ends of the string
print(s.lstrip('h'))  # Strip 'h' from the left end of the string
print(s.rstrip('l'))  # Strip 'l' from the right end of the string

# Other string methods
print(s.index('l'))  # Find the index of the first occurrence of 'l'
print(s.index('l', 2))  # Find the index of 'l' starting from index 2
print(s.index('l', 2, 4))  # Find the index of 'l' between index 2 and 4

# String conversions
print(str(123))  # Convert an integer to a string
print(str(123.45))  # Convert a float to a string
print(str([1, 2, 3]))  # Convert a list to a string
print(str((1, 2, 3)))  # Convert a tuple to a string
print(str({1, 2, 3}))  # Convert a set to a string
print(str({1: 2, 3: 4}))  # Convert a dictionary to a string
print(str(True))  # Convert a boolean to a string
print(str(False))  # Convert a boolean to a string
print(str(None))  # Convert None to a string

# String formatting
print('hello')  # Print a simple string
print('hello %s' % ('world'))  # Format a string using the % operator
print('hello %s' % (123))  # Format an integer as a string
print('hello %d' % (123))  # Format an integer
print('hello %f' % (123.45))  # Format a float
print('hello %e' % (123.45))  # Format a float in scientific notation
print('hello %g' % (123.45))  # Format a float in general format
print('hello %x' % (123))  # Format an integer in hexadecimal
print('hello %o' % (123))  # Format an integer in octal
print('hello %r' % (123))  # Format an integer using repr()
print('hello %s %d %f %e %g %x %o %r' % ('world', 123, 123.45, 123.45, 123.45, 123, 123, 123))  # Format multiple values

# String formatting using the format method
print('hello')  # Print a simple string
print('hello {}'.format('world'))  # Format a string using the format method
print('hello {}'.format(123))  # Format an integer
print('hello {:d}'.format(123))  # Format an integer
print('hello {:f}'.format(123.45))  # Format a float
print('hello {:e}'.format(123.45))  # Format a float in scientific notation
print('hello {:g}'.format(123.45))  # Format a float in general format
print('hello {:x}'.format(123))  # Format an integer in hexadecimal
print('hello {:o}'.format(123))  # Format an integer in octal
print('hello {!r}'.format(123))  # Format an integer using repr()
print('hello {} {:d} {:f} {:e} {:g} {:x} {:o} {!r}'.format('world', 123, 123.45, 123.45, 123.45, 123, 123, 123))  # Format multiple values
print('hello {0} {1} {2} {3} {4} {5} {6} {7}'.format('world', 123, 123.45, 123.45, 123.45, 123, 123, 123))  # Format multiple values using positional arguments

# String formatting using f-strings
print('hello')  # Print a simple string
print(f'hello {"world"}')  # Format a string using an f-string
print(f'hello {123}')  # Format an integer
print(f'hello {123:d}')  # Format an integer
print(f'hello {123:f}')  # Format a float
print(f'hello {123:e}')  # Format a float in scientific notation
print(f'hello {123:g}')  # Format a float in general format
print(f'hello {123:x}')  # Format an integer in hexadecimal
print(f'hello {123:o}')  # Format an integer in octal
print(f'hello {123!r}')  # Format an integer using repr()
print(f'hello {"world"} {123} {123.45} {123.45} {123.45} {123} {123} {123!r}')  # Format multiple values

# String formatting using f-strings with expressions
print('hello')  # Print a simple string
print(f'hello {2*3}')  # Format an expression using an f-string
print(f'hello {2**3}')  # Format an expression using an f-string

# Functions like CHR, ORD, ASCII, UNICODE, STR, REPR etc.
print(chr(97))  # Convert an integer to a character
print(ord('a'))  # Convert a character to an integer
print(ord('A'))  # Convert a character to an integer
print(ord('1'))  # Convert a character to an integer
print(ord(' '))  # Convert a character to an integer
print(ord('\n'))  # Convert a character to an integer
print(ord('\t'))  # Convert a character to an integer
print(ord('\r'))  # Convert a character to an integer
print(ord('\b'))  # Convert a character to an integer
print(ord('\f'))  # Convert a character to an integer
print(ord('\v'))  # Convert a character to an integer
print(ord('\a'))  # Convert a character to an integer

# Overview of tuples
t = (1, 2, 3)  # Define a tuple
print(t)  # Print the tuple
print(t[0])  # Print the first element of the tuple
# t[0] = 4  # Uncommenting this line will cause an error because tuples are immutable
print(t)  # Print the tuple
t = (4, 5, 6)  # Reassign the tuple
print(t)  # Print the tuple
t = (1,)  # Define a single-element tuple
print(t)  # Print the tuple
t = ()  # Define an empty tuple
print(t)  # Print the tuple

# Tuples and lists
t = (1, 2, 3)  # Define a tuple
print(t)  # Print the tuple
l = [1, 2, 3]  # Define a list
print(l)  # Print the list
print(t[0])  # Print the first element of the tuple
print(l[0])  # Print the first element of the list
# t[0] = 4  # Uncommenting this line will cause an error because tuples are immutable
l[0] = 4  # Change the first element of the list
print(t)  # Print the tuple
print(l)  # Print the list

# Slicing
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Define a list
print(l)  # Print the list
print(l[0:3])  # Print the first three elements
print(l[3:6])  # Print elements from index 3 to 5
print(l[6:9])  # Print elements from index 6 to 8
print(l[:5])  # Print the first five elements
print(l[5:])  # Print elements from index 5 to the end
print(l[:])  # Print the entire list
print(l[0:10:2])  # Print every second element
print(l[1:10:2])  # Print every second element starting from index 1
print(l[:7:3])  # Print every third element up to index 6
print(l[3::3])  # Print every third element starting from index 3
print(l[::3])  # Print every third element
print(l[::-1])  # Print the list in reverse order
print(l[::-2])  # Print every second element in reverse order
print(l[7:2:-1])  # Print elements from index 7 to 3 in reverse order
print(l[2:7:-1])  # Print an empty list because the step is negative

# Tuple slicing
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Define a tuple
print(t)  # Print the tuple
print(t[0:3])  # Print the first three elements
print(t[3:6])  # Print elements from index 3 to 5
print(t[6:9])  # Print elements from index 6 to 8
print(t[:5])  # Print the first five elements
print(t[5:])  # Print elements from index 5 to the end
print(t[:])  # Print the entire tuple
print(t[0:10:2])  # Print every second element
print(t[1:10:2])  # Print every second element starting from index 1
print(t[:7:3])  # Print every third element up to index 6
print(t[3::3])  # Print every third element starting from index 3
print(t[::3])  # Print every third element
print(t[::-1])  # Print the tuple in reverse order
print(t[::-2])  # Print every second element in reverse order

# Tuple unpacking
t = (1, 2, 3)  # Define a tuple
print(t)  # Print the tuple
a, b, c = t  # Unpack the tuple into variables
print(a)  # Print the first variable
print(b)  # Print the second variable
print(c)  # Print the third variable
a, b, c = 1, 2, 3  # Assign values to variables
print(a)  # Print the first variable
print(b)  # Print the second variable
print(c)  # Print the third variable
a, b, c = [1, 2, 3]  # Unpack a list into variables
print(a)  # Print the first variable
print(b)  # Print the second variable
print(c)  # Print the third variable

# Overview of dictionaries
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
print(d)  # Print the dictionary
print(d['a'])  # Print the value associated with key 'a'
print(d['b'])  # Print the value associated with key 'b'
print(d['c'])  # Print the value associated with key 'c'
d['a'] = 4  # Change the value associated with key 'a'
print(d)  # Print the dictionary
d['d'] = 5  # Add a new key-value pair
print(d)  # Print the dictionary
del d['b']  # Delete the key-value pair with key 'b'
print(d)  # Print the dictionary
print(d.keys())  # Print the keys of the dictionary
print(d.values())  # Print the values of the dictionary
print(d.items())  # Print the key-value pairs of the dictionary
print(d.get('a'))  # Get the value associated with key 'a'
print(d.get('b'))  # Get the value associated with key 'b'
print(d.get('b', 0))  # Get the value associated with key 'b', or 0 if not found
print(d.get('b', 0) + 1)  # Get the value associated with key 'b', or 0 if not found, and add 1
print(d.pop('a'))  # Remove and return the value associated with key 'a'
print(d)  # Print the dictionary
print(d.popitem())  # Remove and return an arbitrary key-value pair
print(d)  # Print the dictionary
d.clear()  # Clear the dictionary
print(d)  # Print the empty dictionary

# Loop through dictionary, list, and tuples
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
for k in d:
    print(k)  # Print each key
for k in d.keys():
    print(k)  # Print each key
for v in d.values():
    print(v)  # Print each value
for k, v in d.items():
    print(k, v)  # Print each key-value pair
l = [1, 2, 3]  # Define a list
for i in l:
    print(i)  # Print each element
t = (1, 2, 3)  # Define a tuple
for i in t:
    print(i)  # Print each element

# Loop through dictionary, list, and tuples using enumerate
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
for i, k in enumerate(d):
    print(i, k)  # Print the index and each key
for i, k in enumerate(d.keys()):
    print(i, k)  # Print the index and each key
for i, v in enumerate(d.values()):
    print(i, v)  # Print the index and each value
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)  # Print the index and each key-value pair
l = [1, 2, 3]  # Define a list
for i, v in enumerate(l):
    print(i, v)  # Print the index and each element
t = (1, 2, 3)  # Define a tuple
for i, v in enumerate(t):
    print(i, v)  # Print the index and each element

# Loop through dictionary, list, and tuples using zip
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for k, v in zip(d.keys(), d.values()):
    print(k, v)  # Print each key-value pair
for k, v in zip(d.keys(), l):
    print(k, v)  # Print each key and corresponding list element
for k, v in zip(d.keys(), t):
    print(k, v)  # Print each key and corresponding tuple element
for v1, v2 in zip(l, t):
    print(v1, v2)  # Print each pair of list and tuple elements
for i, (v1, v2) in enumerate(zip(l, t)):
    print(i, v1, v2)  # Print the index and each pair of list and tuple elements

# Loop through dictionary, list, and tuples using zip and enumerate
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for i, (k, v) in enumerate(zip(d.keys(), d.values())):
    print(i, k, v)  # Print the index and each key-value pair
for i, (k, v) in enumerate(zip(d.keys(), l)):
    print(i, k, v)  # Print the index and each key and corresponding list element
for i, (k, v) in enumerate(zip(d.keys(), t)):
    print(i, k, v)  # Print the index and each key and corresponding tuple element
for i, (v1, v2) in enumerate(zip(l, t)):
    print(i, v1, v2)  # Print the index and each pair of list and tuple elements

# Loop through dictionary, list, and tuples using zip, enumerate, and range
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for i, (k, v) in zip(range(len(d)), zip(d.keys(), d.values())):
    print(i, k, v)  # Print the index and each key-value pair
for i, (k, v) in zip(range(len(d)), zip(d.keys(), l)):
    print(i, k, v)  # Print the index and each key and corresponding list element
for i, (k, v) in zip(range(len(d)), zip(d.keys(), t)):
    print(i, k, v)  # Print the index and each key and corresponding tuple element
for i, (v1, v2) in zip(range(len(l)), zip(l, t)):
    print(i, v1, v2)  # Print the index and each pair of list and tuple elements

# Loop through dictionary, list, and tuples using zip, enumerate, range, and sorted
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for i, (k, v) in zip(range(len(d)), zip(sorted(d.keys()), sorted(d.values()))):
    print(i, k, v)  # Print the index and each sorted key-value pair
for i, (k, v) in zip(range(len(d)), zip(sorted(d.keys()), sorted(l))):
    print(i, k, v)  # Print the index and each sorted key and corresponding list element
for i, (k, v) in zip(range(len(d)), zip(sorted(d.keys()), sorted(t))):
    print(i, k, v)  # Print the index and each sorted key and corresponding tuple element
for i, (v1, v2) in zip(range(len(l)), zip(sorted(l), sorted(t))):
    print(i, v1, v2)  # Print the index and each pair of sorted list and tuple elements

# Loop through dictionary, list, and tuples using foreach
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for k, v in d.items():
    print(k, v)  # Print each key-value pair
for v in l:
    print(v)  # Print each element of the list
for v in t:
    print(v)  # Print each element of the tuple

# Loop through dictionary, list, and tuples using foreach and sorted
d = {'a': 1, 'b': 2, 'c': 3}  # Define a dictionary
l = [1, 2, 3]  # Define a list
t = (1, 2, 3)  # Define a tuple
for k, v in sorted(d.items()):
    print(k, v)  # Print each sorted key-value pair
for v in sorted(l):
    print(v)  # Print each sorted element of the list
for v in sorted(t):
    print(v)  # Print each sorted element of the tuple

# Overview of sets
s = {1, 2, 3}  # Define a set
print(s)  # Print the set
s.add(4)  # Add an element to the set
print(s)  # Print the set
s.update({5, 6, 7})  # Add multiple elements to the set
print(s)  # Print the set
s.remove(1)  # Remove an element from the set
print(s)  # Print the set
s.discard(2)  # Discard an element from the set
print(s)  # Print the set
s.pop()  # Remove and return an arbitrary element from the set
print(s)  # Print the set
s.clear()  # Clear the set
print(s)  # Print the empty set
s = {1, 2, 3}  # Define a set
print(s)  # Print the set
s1 = {4, 5, 6}  # Define another set
print(s1)  # Print the set
print(s.union(s1))  # Print the union of the sets
print(s.intersection(s1))  # Print the intersection of the sets
print(s.difference(s1))  # Print the difference of the sets
print(s.symmetric_difference(s1))  # Print the symmetric difference of the sets
print(s.issubset(s1))  # Check if s is a subset of s1
print(s.issuperset(s1))  # Check if s is a superset of s1
print(s.isdisjoint(s1))  # Check if s and s1 are disjoint
print(s.copy())  # Print a copy of the set
print(s1.copy())  # Print a copy of the set
print(s)  # Print the set
print(s1)  # Print the set
s.update(s1)  # Update s with elements from s1
print(s)  # Print the set

# Set operations
s = {1, 2, 3}  # Define a set
print(s)  # Print the set
s1 = {4, 5, 6}  # Define another set
print(s1)  # Print the set
print(s | s1)  # Print the union of the sets
print(s & s1)  # Print the intersection of the sets
print(s - s1)  # Print the difference of the sets
print(s ^ s1)  # Print the symmetric difference of the sets
print(s <= s1)  # Check if s is a subset of s1
print(s >= s1)  # Check if s is a superset of s1
print(s.isdisjoint(s1))  # Check if s and s1 are disjoint

# Set operations using functions
s = {1, 2, 3}  # Define a set
print(s)  # Print the set
s1 = {4, 5, 6}  # Define another set
print(s1)  # Print the set
print(s.union(s1))  # Print the union of the sets
print(s.intersection(s1))  # Print the intersection of the sets
print(s.difference(s1))  # Print the difference of the sets
print(s.symmetric_difference(s1))  # Print the symmetric difference of the sets
print(s.issubset(s1))  # Check if s is a subset of s1
print(s.issuperset(s1))  # Check if s is a superset of s1
print(s.isdisjoint(s1))  # Check if s and s1 are disjoint

# Overview of deque
from collections import deque  # Import deque from collections module
d = deque([1, 2, 3])  # Define a deque
print(d)  # Print the deque
d.append(4)  # Append an element to the right end of the deque
print(d)  # Print the deque
d.appendleft(0)  # Append an element to the left end of the deque
print(d)  # Print the deque
d.pop()  # Remove and return an element from the right end of the deque
print(d)  # Print the deque
d.popleft()  # Remove and return an element from the left end of the deque
print(d)  # Print the deque
d.extend([3, 4, 5])  # Extend the deque by appending elements to the right end
print(d)  # Print the deque
d.extendleft([2, 1, 0])  # Extend the deque by appending elements to the left end
print(d)  # Print the deque
d.rotate(1)  # Rotate the deque to the right by 1 position
print(d)  # Print the deque
d.rotate(-1)  # Rotate the deque to the left by 1 position
print(d)  # Print the deque
d.clear()  # Clear the deque
print(d)  # Print the empty deque

# Stack in Python
s = []  # Define an empty list to use as a stack

# Push operation: Add an element to the top of the stack
def push(s, x):
    s.append(x)

# Pop operation: Remove and return the top element of the stack
def pop(s):
    return s.pop()

# Top operation: Return the top element of the stack without removing it
def top(s):
    return s[-1]

# Empty operation: Check if the stack is empty
def empty(s):
    return len(s) == 0

# Size operation: Return the number of elements in the stack
def size(s):
    return len(s)

# Example usage of stack operations
s = []  # Define an empty stack
print(s)  # Print the empty stack
push(s, 1)  # Push 1 onto the stack
print(s)  # Print the stack
push(s, 2)  # Push 2 onto the stack
print(s)  # Print the stack
push(s, 3)  # Push 3 onto the stack
print(s)  # Print the stack
print(top(s))  # Print the top element of the stack
print(pop(s))  # Pop and print the top element of the stack
print(s)  # Print the stack

# Tree in Python
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None

# Example of creating a binary tree
root = Node(1)  # Create the root node with data 1
root.left = Node(2)  # Create the left child of the root with data 2
root.right = Node(3)  # Create the right child of the root with data 3
root.left.left = Node(4)  # Create the left child of the left child with data 4
root.left.right = Node(5)  # Create the right child of the left child with data 5
root.right.left = Node(6)  # Create the left child of the right child with data 6
root.right.right = Node(7)  # Create the right child of the right child with data 7
print(root.data)  # Print the data of the root node
print(root.left.data)  # Print the data of the left child of the root
print(root.right.data)  # Print the data of the right child of the root

# Tree traversal in Python
# Inorder traversal: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)  # Traverse the left subtree
        print(root.data)  # Print the data of the root
        inorder(root.right)  # Traverse the right subtree

# Preorder traversal: Root, Left, Right
def preorder(root):
    if root:
        print(root.data)  # Print the data of the root
        preorder(root.left)  # Traverse the left subtree
        preorder(root.right)  # Traverse the right subtree

# Postorder traversal: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)  # Traverse the left subtree
        postorder(root.right)  # Traverse the right subtree
        print(root.data)  # Print the data of the root

# Horizontal tree traversal (Level order)
def levelorder(root):
    q = []  # Define an empty queue
    q.append(root)  # Enqueue the root node
    while len(q) != 0:
        temp = q.pop(0)  # Dequeue a node
        print(temp.data)  # Print the data of the node
        if temp.left:
            q.append(temp.left)  # Enqueue the left child
        if temp.right:
            q.append(temp.right)  # Enqueue the right child

# Size of the tree: Number of nodes
def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# Height of the tree: Longest path from root to leaf
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Number of leaf nodes: Nodes with no children
def leafnodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return leafnodes(root.left) + leafnodes(root.right)

# Number of non-leaf nodes: Nodes with at least one child
def nonleafnodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + nonleafnodes(root.left) + nonleafnodes(root.right)

# Example usage of tree traversal and properties
root = Node(1)  # Create the root node with data 1
root.left = Node(2)  # Create the left child of the root with data 2
root.right = Node(3)  # Create the right child of the root with data 3
root.left.left = Node(4)  # Create the left child of the left child with data 4
root.left.right = Node(5)  # Create the right child of the left child with data 5
root.right.left = Node(6)  # Create the left child of the right child with data 6
root.right.right = Node(7)  # Create the right child of the right child with data 7
print("Inorder")
inorder(root)  # Perform inorder traversal
print("Preorder")
preorder(root)  # Perform preorder traversal
print("Postorder")
postorder(root)  # Perform postorder traversal
print("Levelorder")
levelorder(root)  # Perform level order traversal
print("Size of tree")
print(size(root))  # Print the size of the tree
print("Height of tree")
print(height(root))  # Print the height of the tree
print("Number of leaf nodes")
print(leafnodes(root))  # Print the number of leaf nodes
print("Number of non-leaf nodes")
print(nonleafnodes(root))  # Print the number of non-leaf nodes

# Binary Search Tree in Python
class Node:
    def __init__(self, data):
        self.data = data  # Store the data in the node
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None

    def __str__(self) -> str:
        return str(self.data)  # Return the string representation of the node

# Insert a node into the binary search tree
def insert(root, data):
    if root is None:
        return Node(data)  # Create a new node if the root is None
    if data < root.data:
        root.left = insert(root.left, data)  # Insert into the left subtree
    else:
        root.right = insert(root.right, data)  # Insert into the right subtree
    return root

# Search for a node in the binary search tree
def search(root, data):
    if root is None or root.data == data:
        return root  # Return the node if found or None if not found
    if root.data < data:
        return search(root.right, data)  # Search in the right subtree
    return search(root.left, data)  # Search in the left subtree

# Example usage of binary search tree
root = None  # Initialize the root as None
root = insert(root, 50)  # Insert nodes into the binary search tree
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
print(search(root, 50))  # Search for a node and print the result
print(search(root, 30))
print(search(root, 80))

# Graph in Python
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to store the graph

    # Add an edge to the graph
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []  # Initialize an empty list if the vertex is not in the graph
        self.graph[u].append(v)  # Add the edge to the graph

    # Print the graph
    def printGraph(self):
        print("Graph:")
        for i in self.graph:
            print(f"  {i} --> {self.graph[i]}")  # Print each vertex and its edges

# Example usage of graph
g = Graph()  # Create a graph
g.addEdge(0, 1)  # Add edges to the graph
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()  # Print the graph