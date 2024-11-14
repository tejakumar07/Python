from calculator import square

def main():
    test_square()
def test_square():
    if square(2)!=4:
        print("2 Square did not work")
    if square(3)!=9:
        print("3 Square did not work") #Here Only this only Error sin 2*2==2+2

if __name__=="__main__":
    main()