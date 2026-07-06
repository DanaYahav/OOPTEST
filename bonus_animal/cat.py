
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