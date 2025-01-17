from hello import hello

def test_arguments():
    assert hello("Teja") == "hello, Teja"
    assert hello("Kumar") == "hello, Kumar"
    assert hello("Apple") == "hello, Apple"

def test_default():
    assert hello() == "hello, World"