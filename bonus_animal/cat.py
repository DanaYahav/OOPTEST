
from typing import override

from animal import Animal
from pet import Pet


class Cat(Animal, Pet):

    def __init__(self, name):
        super().__init__(4)
        self.name = name


    def get_name(self):
        return self.name

    @override
    def set_name(self, name):
        self.name = name

    @override
    def play(self):
        print("Cat is playing")

    @override
    def eat(self):
        print("Cat is eating")

    from typing import override

    @override
    def __str__(self):
        return (f"Animal : Cat\n" 
                f"Name : {self.get_name()}\n" 
                f"Legs  : 4")