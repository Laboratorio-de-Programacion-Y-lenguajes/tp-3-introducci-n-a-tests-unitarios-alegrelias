"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


#   - Raíz de 0 (resultado: 0.0)
def test_raiz_cero():
    assert sqrt(0) == 0
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
def test_raiz_inexacta():
    assert type(sqrt(2)) == float
#   - Raíz de un número negativo → debe lanzar ValueError
def test_numero_imaginario():
    with pytest.raises(ValueError):
        sqrt(-4)
