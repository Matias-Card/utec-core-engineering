#!/usr/bin/env python3
"""Demostración de herencia y polimorfismo en Python."""


class Animal:
    """Clase padre que representa un animal."""

    def speak(self):
        """Devuelve un sonido genérico."""
        return "Some sound"


class Dog(Animal):
    """Representa un perro."""

    def speak(self):
        """Devuelve el sonido de un perro."""
        return "Woof"


class Cat(Animal):
    """Representa un gato."""

    def speak(self):
        """Devuelve el sonido de un gato."""
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
