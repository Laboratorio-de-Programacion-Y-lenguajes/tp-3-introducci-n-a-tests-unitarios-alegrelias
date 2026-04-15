"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


#   - Cualquier número elevado a 0 (resultado: 1)
def test_potencia_cero():
    assert pow_(2, 0) == 1
#   - Número elevado a 1 (resultado: el mismo número)
def test_potencia_uno():
    assert pow_(2, 1) == 2
#   - Base negativa con exponente par (resultado positivo)
def test_base_negativa_exp_par():
    assert pow_(-2, 2) == 4
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
def test_base_decimal():
    assert pow_(9, 0.5) == 3
