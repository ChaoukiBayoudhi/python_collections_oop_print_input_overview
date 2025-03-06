# Import datetime library with alias 'dt' for date/time operations
import datetime as dt

# Define a class named Person to represent individual people
class Person:
    # Constructor method to initialize a Person object with their details
    # Parameters have default values: birthdate defaults to current time, email and address default to None
    def __init__(self,name,familyName,birthdate=dt.datetime.now,email=None,address=None) -> None:
        self.name=name
        self.familyName=familyName
        self.birthdate=birthdate
        self.email=email
        self.address=address

    # Define string representation of the Person object
    # Returns formatted string with name and email
    def __str__(self) -> str:
        return f'name = {self.name+" "+self.familyName},email = {self.email}'

# Create first example: Person object with name and birthdate
p1=Person('Ahmed','Ben Mohamed',dt.datetime(2020,3,17))
# Print the first person's details
print(p1)

# Create second example: Person object with name and email
#other way tio instantiate objects
p2=Person(name='Bochra',
          familyName='Bayoudhi',
          email='bochra@isg.tn')
# Print the second person's details
print(p2)


# Import datetime library with alias 'dt' for date/time operations
import datetime as dt

# Define a class named Student to represent student information
class Student:
    # Constructor method to initialize a Student object with their details
    def __init__(self,name,familyName,studentId,major,birthdate=dt.datetime.now,email=None,address=None) -> None:
        # Private fields are prefixed with double underscore
        self.__name = name
        self.__familyName = familyName
        self.__studentId = studentId
        self.__major = major
        self.__birthdate = birthdate
        self.__email = email
        self.__address = address

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter and Setter for familyName
    @property
    def familyName(self):
        return self.__familyName
    
    @familyName.setter
    def familyName(self, value):
        self.__familyName = value

    # Getter and Setter for studentId
    @property
    def studentId(self):
        return self.__studentId
    
    @studentId.setter
    def studentId(self, value):
        self.__studentId = value

    # Getter and Setter for major
    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self, value):
        self.__major = value

    # Getter and Setter for birthdate
    @property
    def birthdate(self):
        return self.__birthdate
    
    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value

    # Getter and Setter for email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    # Getter and Setter for address
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        self.__address = value

    # Define string representation of the Student object
    def __str__(self) -> str:
        return f'name = {self.__name+" "+self.__familyName}, ID = {self.__studentId}, major = {self.__major}'


# Creating a student
s1 = Student('Ahmed', 'Ben Mohamed', '12345', 'Computer Science')

# Getting values using getters
print(s1.name)  # Uses the @property getter
print(s1.major)  # Uses the @property getter

# Setting values using setters
s1.major = "Data Science"  # Uses the @major.setter
s1.email = "ahmed@example.com"  # Uses the @email.setter