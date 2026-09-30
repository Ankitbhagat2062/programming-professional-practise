class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sound(self):
        print(f'{self.name} who is {self.age} years old is making sound')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d= Dog('max',4)
d.sound()
c = Cat("meow", "5")
c.sound()

