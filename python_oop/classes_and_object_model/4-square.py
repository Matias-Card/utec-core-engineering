#!/usr/bin/env python3
"""Define la clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado mediante su tamaño."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con un tamaño determinado."""
        self.size = size

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

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2
