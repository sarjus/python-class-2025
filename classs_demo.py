class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"


dog1 = Dog("abc",2)
print(dog1.description())