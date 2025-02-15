def main():
    student = get_student()
    if student['name'] == 'Harry':
        student['house'] = 'Griffindor'
    print(f"{student["name"]} from {student["house"]}")
def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    return {'name':name,'house':house}
if __name__ == "__main__":
    main()