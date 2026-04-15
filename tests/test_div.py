"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


#   - División que da resultado decimal (float)
def test_div_decimal():
    assert div(1, 4) == 0.25
#   - División con números negativos
def test_div_negativo():
    assert div(-1, 4) == -0.25
#   - División por cero → debe lanzar ZeroDivisionError
def test_error_div_cero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

