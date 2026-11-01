#!/usr/bin/env python3
"""Define la clase Rectangle que representa un rectángulo."""


class Rectangle:
    """Representa un rectángulo mediante su ancho y alto."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo con ancho y alto."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho después de validar el valor."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto después de validar el valor."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
