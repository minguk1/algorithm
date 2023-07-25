from datetime import  date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_age(cls, name, birth_year):
        name1 = name
        age = date.today().year - birth_year
        return cls(name1, age)




    def check_age(self):
        if self.age <= 19:
            return True
        else:
            return False



#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age)
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
