#In this we are using Pytest
#Offical documentation URL: docs.pytest.org
from calculator import square

def test_square():
    assert square(5)==25
    assert square(3)==9  #here this assertion fails automatically pytest will not test the other
    assert square(2) == 4
    assert square(0)==0
    assert square(-1)==1
    assert square(-2)==4
    assert square(-3)==9

"""
For Some Reasons Pytest not supporting in my PC
It will not Exactly say how  to solve the Error
It will say There is success in program or not
"""

#lets fix this in next program