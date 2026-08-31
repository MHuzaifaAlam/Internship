class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return f"{self.name} makes a sound "

class Dog(Animal):
    bark="Woof Woof Woof Woof"

jack=Dog('Jack')
print(jack.sound())
print(jack.bark)
