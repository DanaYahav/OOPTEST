from typing import override
from animal import Animal
from pet import Pet


class Fish(Animal, Pet):

    def __init__(self):
        super().__init__(0)
        self.__name = ""

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @override
    def play(self):
        print("Fish is playing")

    @override
    def walk(self):
        print("Fish can't walk")

    @override
    def eat(self):
        print("Fish is eating")

    from typing import override

    @override
    def __str__(self):
        return (f"Animal : Fish\n" 
                f"Name   : {self.get_name()}\n" 
                f"Legs   : 0")