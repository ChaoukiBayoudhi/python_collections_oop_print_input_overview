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
        # Make sure birthdate is a datetime object
        if isinstance(value, str):
            # If birthdate is a string, convert it to datetime
            self.__birthdate = dt.datetime.strptime(value, '%Y-%m-%d')
        elif isinstance(value, dt.datetime):
            self.__birthdate = value
        else:
            raise ValueError("birthdate must be a datetime object or a string in 'YYYY-MM-DD' format")

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
    
    # Define a method to calculate the student's age in years, months and days
    def age(self):
        # Make sure self.__birthdate is a datetime object, not a method
        if callable(self.__birthdate):
            current_birthdate = self.__birthdate()
        else:
            current_birthdate = self.__birthdate

        # Calculate the difference between the current date and the student's birthdate
        delta = dt.datetime.now() - current_birthdate
        # Calculate the age in years, months and days
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        return years, months, days

    #other version of age function using predefined functions
    def age2(self):
        if callable(self.__birthdate):
            current_birthdate = self.__birthdate()
        else:
            current_birthdate = self.__birthdate
        return divmod((dt.datetime.now() - current_birthdate).days, 365)
    



# Creating a student
s1 = Student('Ahmed', 'Ben Mohamed', '12345', 'Computer Science')

# Getting values using getters
print(s1.name)  # Uses the @property getter
print(s1.major)  # Uses the @property getter

# Setting values using setters
s1.major = "Data Science"  # Uses the @major.setter
s1.email = "ahmed@example.com"  # Uses the @email.setter

#Example of using the age method
print(s1.age())
print(s1.age2())

#Example of inheritance
class Teacher(Person):
    def __init__(self, name, familyName, birthdate, email, address, subject, salary):
        super().__init__(name, familyName, birthdate, email, address)
        self.subject = subject
        self.salary = salary

    def __str__(self):
        return f'name = {self.name+" "+self.familyName}, email = {self.email}, subject = {self.subject}, salary = {self.salary}'
        #or using the parent class method
        #return super().__str__() + f", subject = {self.subject}, salary = {self.salary}"
    
    def increase_salary(self, amount):
        self.salary += amount

# Create a Teacher object using arabic names written in latin characters
t1 = Teacher(name='Ahmed', 
                familyName='Ben Mohamed', 
                birthdate=dt.datetime(1980, 3, 17),
                email = 'ahmed.benmohamed@isg.tn',
                address = 'Tunis, Tunisia',
                subject = 'Computer Science', 
                salary = 50000
                )
# Print the teacher's details
print(t1)
t1.increase_salary(5000)
print(t1)
