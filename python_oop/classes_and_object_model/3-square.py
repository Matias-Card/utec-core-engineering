#!/usr/bin/env python3
"""Define la clase Square que representa un cuadrado."""


class Square:
    """Representa un cuadrado mediante su tamaño."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con un tamaño determinado."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2
