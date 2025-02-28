#x=int(input("Entrez un nombre: "))
#y=int(input("Entrez un nombre: "))
nom=input("Entrez votre nom: ")

moy=float(input("Entrez votre moyenne: "))
print("Bonjour",nom)
print("Votre moyenne est de ",moy)
#print(x,y)
#print("x=",x," et y=",y)

# {0:d} is a placeholder for an integer
# {0:f} for a float
# {0:s} for a string
# {0:x} for a hexadecimal
# {0:o} for an octal
# {0:e} for scientific notation
# {0:g} for a general number
# {0:c} for a character (requires an integer)
# {0!r} for a string representation
# {0!a} for an ASCII representation
# {0:u} is not used in Python, use {0:d} for unsigned integers
# {0:i} is not used in Python, use {0:d} for integers

#Examples
value = 42
print(f"Integer: {value:d}")
print(f"Float: {value:f}")
print(f"String: {'example':s}")
print(f"Hexadecimal: {value:x}")
print(f"Octal: {value:o}")
print(f"Scientific: {value:e}")
print(f"General: {value:g}")
print(f"Character: {chr(value)}")
print(f"String representation: {value!r}")
print(f"ASCII representation: {value!a}")

#print use of sep and end
print("Hello", "world", sep=", ", end="!\n")
#more examples
#print Pascal's triangle using sep and end
for i in range(10):
    print(11**i, sep=", ", end="!\n")

#print the Fibonacci sequence using sep and end
a, b = 0, 1
for i in range(10):
    print(a, end=", ")
    a, b = b, a + b
print()
#Print a matrix using sep and end
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    print(*row, sep=", ", end="\n")


#The print function can also be used to write to a file
with open("output.txt", "w") as file:
    print("Hello, world!", file=file)


