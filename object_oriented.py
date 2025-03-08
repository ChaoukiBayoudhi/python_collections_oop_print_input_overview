# Import datetime library with alias 'dt' for date/time operations
import datetime as dt
from abc import ABC, abstractmethod

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


#Example of polymorphism, multiple inheritance and method overriding
# Define a class named MeansOfTransport to represent different types of vehicles
#include protected fields
#Design is an abstract class that is inherited by Bicycle and Car
#MeansOfTransport is an abstract class that is inherited by Bicycle and Car
#Bicycle and Car are concrete classes
#use decorators to define abstract methods and properties
#use super() to call parent class methods
#use method overriding to change the behavior of inherited methods
#use polymorphism to call the same method on different objects
class MeansOfTransport(ABC):
    """Base class for all transportation vehicles. Defines common properties and behaviors."""
    def __init__(self, name: str, max_speed: float):
        # Protected attributes with underscore prefix
        self._name = name          # Name of the vehicle
        self._max_speed = max_speed  # Maximum speed in km/h

    def __str__(self) -> str:
        # String representation of the vehicle
        return f'{self._name} with max speed of {self._max_speed} km/h'

    # Abstract methods that must be implemented by child classes
    @abstractmethod
    def move(self) -> str:
        """Define how the vehicle moves"""
        pass

    """
    #without using decorators
    def move(self) -> str:
        '''Method for movement'''
        raise NotImplementedError("Subclasses must implement this method")
    """
    
    @abstractmethod
    def stop(self) -> str:
        """Define how the vehicle stops"""
        pass
    
    @abstractmethod
    def turn(self, direction: str) -> str:
        """Define how the vehicle turns"""
        pass

class Design(ABC):
    """Handles the appearance and material properties of vehicles"""
    def __init__(self, color: str, material: str):
        self._color = color        # Color of the vehicle
        self._material = material  # Main material used in construction

    def __str__(self) -> str:
        return f'{self.color} {self.material}'

    # Property decorators for controlled access to attributes
    @property
    def color(self) -> str:
        """Get the color of the vehicle"""
        return self._color 
    
    @color.setter
    def color(self, value):
        """Set the color of the vehicle with validation"""
        if not isinstance(value, str):
            raise ValueError("Color must be a string")
        self._color = value
    
    @property
    def material(self) -> str:
        """Get the material of the vehicle"""
        return self._material
    
    @material.setter
    def material(self, value):
        """Set the material of the vehicle with validation"""
        if not isinstance(value, str):
            raise ValueError("Material must be a string")
        self._material = value

class Bicycle(MeansOfTransport, Design):
    """Represents a bicycle - inherits from both MeansOfTransport and Design"""
    def __init__(self, name: str, max_speed: float, color: str, material: str):
        # Initialize both parent classes
        MeansOfTransport.__init__(self, name, max_speed)
        Design.__init__(self, color, material)
    
    # Implementation of required abstract methods
    def move(self) -> str:
        """Describes how a bicycle moves"""
        return 'Pedal to move the bicycle'
    
    def stop(self) -> str:
        """Describes how a bicycle stops"""
        return 'Apply the brakes to stop the bicycle'
    
    def turn(self, direction: str) -> str:
        """Describes how a bicycle turns"""
        return f'Turn the handlebars {direction} to turn the bicycle'

    def __str__(self) -> str:
        """Combined string representation of transport and design properties"""
        return f'{super().__str__()} with {Design.__str__(self)}'

class Car(MeansOfTransport, Design):
    """Represents a car with additional car-specific properties"""
    def __init__(self, 
                 name: str, 
                 max_speed: float, 
                 color: str, 
                 material: str, 
                 wheels: int = 4,           # Number of wheels
                 doors: int = 4,            # Number of doors
                 seats: int = 5,            # Number of seats
                 engine: str = 'V6',        # Engine type
                 fuel: str = 'Gasoline',    # Fuel type
                 transmission: str = 'Automatic'):  # Transmission type
        # Initialize parent classes
        MeansOfTransport.__init__(self, name, max_speed)
        Design.__init__(self, color, material)
        
        # Car-specific attributes
        self.wheels = wheels
        self.doors = doors
        self.seats = seats
        self.engine = engine
        self.fuel = fuel
        self.transmission = transmission
    
    # Implementation of required abstract methods
    def move(self) -> str:
        """Describes how a car moves"""
        return 'Press the accelerator to move the car'
    
    def stop(self) -> str:
        """Describes how a car stops"""
        return 'Press the brake pedal to stop the car'
    
    def turn(self, direction: str) -> str:
        """Describes how a car turns"""
        return f'Turn the steering wheel {direction} to turn the car'
    
    def __str__(self) -> str:
        """Combined string representation of transport and design properties"""
        return f'{super().__str__()} with {Design.__str__(self)}'

# Example usage of the classes
if __name__ == "__main__":
    # Create a bicycle instance
    bike = Bicycle(
        name="Mountain Bike",
        max_speed=30,
        color="red",
        material="aluminum"
    )
    print(bike)                    # Display bicycle details
    print(bike.move())            # Show how bicycle moves
    print(bike.turn("left"))      # Show how bicycle turns
    
    # Create a car instance
    car = Car(
        name="Sedan",
        max_speed=200,
        color="blue",
        material="steel"
    )
    print(car)                    # Display car details
    print(car.move())            # Show how car moves
    print(car.turn("right"))     # Show how car turns
