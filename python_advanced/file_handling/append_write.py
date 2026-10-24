#!/usr/bin/env python3
"""Añade texto al final de un archivo de texto."""


def append_write(filename="", text=""):
    """Añade texto a un archivo y devuelve los caracteres añadidos."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
