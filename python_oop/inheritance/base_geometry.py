#!/usr/bin/env python3
"""Define la clase base para figuras geométricas."""


class BaseGeometry:
    """Representa una geometría básica."""

    def area(self):
        """Indica que el cálculo del área no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
