from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) ==4
    assert square(3) ==9 #Here assert is the keyword that should definately work(True) otherwise it will give error

if __name__ == "__main__":
    main()

#It will give a new Error called AssertionError let's try to fix it in the next program