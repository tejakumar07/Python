from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_arguments():
    for name in ["teja","apple","harry","hermione","apple"]:
        assert hello(name) == f"hello, {name}"