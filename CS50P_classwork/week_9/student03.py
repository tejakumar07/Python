def main():
    student = get_student()
    if student[0] == 'Harry' and student[1] != "Griffindor":
        student[1] = 'Griffindor'
        print(f"{student[0]} from {student[1]}")
def get_student():
    name= input("Name: ").title()
    house = input("House: ").title()
    # return (name, house) #Tuple
    # to fix this we use list
    return [name,house]
if __name__ == "__main__":
    main()
# It will give you the error.
# Tuple are Immutable.
# tuple object does not support item assignment.
# over tuple vs list