"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


#   - Multiplicar por cero
def test_mul_cero():
    assert mul(2, 0) == 0
#   - Multiplicar dos números negativos (resultado positivo)
def test_mul_negativo():
    assert mul(-2, -2) == 4
#   - Multiplicar un positivo y un negativo (resultado negativo)
def test_mul_positivo_negativo():
    assert mul(-2, 2) == -4
#   - Multiplicar por 1 (elemento neutro)
def test_mul_neutra():
    assert mul(2, 1) == 2
#   - Multiplicar dos decimales (float)
def test_mul_decimal():
    assert mul(20, 1.5) == 30.0
