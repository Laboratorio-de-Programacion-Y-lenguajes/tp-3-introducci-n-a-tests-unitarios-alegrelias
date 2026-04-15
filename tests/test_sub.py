"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


#   - Restar un número mayor al primero (resultado negativo)
def test_suma_mayor_menor():
    assert sub(2, 5) == -3
#   - Restar cero
def test_resta_cero():
    assert sub(2, 0) == 2
#   - Restar dos números negativos
def test_resta_negativa():
    assert sub(-2, -2) == 0
#   - Restar dos números decimales (float)
def test_resta_decimal():
    assert sub(2.5, 1) == 1.5
