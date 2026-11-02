#!/usr/bin/env python3
"""Define la clase Square."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño válido."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
