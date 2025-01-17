from calculator import square

def test_postive_square():
    assert square(2)==4
    assert square(3)==9
    assert square(4)==16
    assert square(5)==25
def test_negative_square():
    assert square(-1)==1
    assert square(-2)==4
    assert square(-3)==9
    assert square(-4)==16
def test_zero_square():
    assert square(0)==0

