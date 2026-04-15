"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
def test_lista_elemento_unico():
    assert mean([10]) == 10
#   - Lista con números negativos
def test_promedio_negativo():
    assert mean([-1, -1, -1, 10]) == 1.75
#   - Lista con números decimales (float)
def test_lista_decimal():
    assert mean([2.5, 2.5, 2.5]) == 2.5
#   - Lista vacía → debe lanzar ValueError
def test_lista_vacia():
    with pytest.raises(ValueError):
        assert mean([])
