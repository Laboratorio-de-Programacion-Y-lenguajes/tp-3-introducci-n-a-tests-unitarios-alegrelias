"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add

def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


#   - Sumar dos números negativos
def test_add_suma_negativa():
    assert add(-1, -1) == -2
#   - Sumar un número positivo y uno negativo
def test_add_positivo_negativo():
    assert add(-1, 8) == 7
#   - Sumar con cero
def test_add_suma_cero():
    assert add(1, 0) == 1
#   - Sumar dos números decimales (float)
def test_add_suma_decimal():
    assert add(2.5, 2.5) == 5.0
