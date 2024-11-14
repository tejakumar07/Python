from calculator import square

def main():

    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square is not 4") #As we know that 2*2==2+2
        print("Test Case Failed")
    try:
        assert square(3)==9
    except AssertionError:
        print("3 square is not 9")#But here 3*3!=3+3
        print("Test Case Failed")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square is not 4")
        print("Test Case Failed")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square is not 9")
        print("Test Case Failed")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 square is not 0")
        print("Test Case Failed")


if __name__ == "__main__":
    main()