#define class Person
class Person:
    def __init__(self,name,familyName,birthdate,email=None,address=None) -> None:
        self.name=name
        self.familyName=familyName
        self.birthdate=birthdate
        self.email=email
        self.address=address

    def __str__(self) -> str:
        return f'name = {self.name+" "+self.familyName},email = {self.email}'
#example of use
