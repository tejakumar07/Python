import pytest

from calculator1 import square

def test_postive():
    assert square(2) ==4
    assert square(3) ==9
    assert square(4) ==16
def test_negative():
    assert square(-1) ==1
    assert square(-2) ==4
    assert square(-3) ==9
def test_zero():
    assert square(0) ==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
