#!/usr/bin/env python3
"""Define un rectángulo con área y representación en cadena."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa el rectángulo con dimensiones válidas."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripción del rectángulo."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
