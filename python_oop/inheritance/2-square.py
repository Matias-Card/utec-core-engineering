#!/usr/bin/env python3
"""Define la clase Square con representación en cadena."""

Square = __import__('1-square').Square


class Square(Square):
    """Representa un cuadrado con descripción personalizada."""

    def __str__(self):
        """Devuelve la descripción del cuadrado."""
        return "[Square] {}/{}".format(
            self._Square__size, self._Square__size
        )
