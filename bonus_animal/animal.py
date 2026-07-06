from abc import ABC


class Animal(ABC):

    def __init__(self, legs):
        self._legs = legs

    def walk(self):
        print(f"Walking on {self._legs} legs")

    def eat(self):
        print("Animal is eating")