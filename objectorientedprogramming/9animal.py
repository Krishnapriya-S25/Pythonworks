class Animal:
    name:str
    species:str
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def __str__(self):
        return self.name
class Lion(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    def sound(self):
        print("roar")
lion_instance=Lion("lion","carnivores")
print(lion_instance)
print(lion_instance.sound())

class Cat(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    def sound(self):
        print("meow")
cat_instance=Cat("cat","omnivores")
print(cat_instance)
print(cat_instance.sound())



