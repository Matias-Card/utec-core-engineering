#!/usr/bin/env python3
"""Define la clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado mediante su tamaño y posición."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Actualiza el tamaño después de validar el valor."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Actualiza la posición después de validar la tupla."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(type(num) is int and num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado respetando su posición."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Devuelve la representación textual del cuadrado."""
        if self.__size == 0:
            return ""

        rows = [
            " " * self.__position[0] + "#" * self.__size
            for _ in range(self.__size)
        ]

        return "\n" * self.__position[1] + "\n".join(rows)
