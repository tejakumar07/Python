def main():
    row = int(input("Enter No. of rows: "))
    column = int(input("Enter No. of columns: "))
    print_square(row,column)

def print_square(row,column):
    for i in range(row):
        #One Loop is used for Column another One for Row
        for j in range(column):
            print(" # ",end="")
        print("")

main()