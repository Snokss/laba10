class Person:
    def __init__(self, name, surname, age, address, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone = phone

class PersonBuilder:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.address = None
        self.phone = None

    def set_name(self, name):
        self.name = name
        return self

    def set_surname(self, surname):
        self.surname = surname
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_address(self, address):
        self.address = address
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def build(self):
        return Person(self.name, self.surname, self.age, self.address, self.phone)
    

person = PersonBuilder().set_name('John').set_surname('Doe').set_age(30).set_address('123 Main St').set_phone('555-1234').build()

print(person.name)   
print(person.surname) 
print(person.age)     
print(person.address)
print(person.phone) 