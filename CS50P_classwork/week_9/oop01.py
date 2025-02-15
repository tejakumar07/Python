# Official documentation
# docs.python.org/3/tutorial/classes.html

class Student: # Classes are like BluePrint
    ...
def main():
    student = get_student()
    print(f'{student.name} from {student.house}')
def get_student():
    student = Student() # Creating an Object
    student.name = input("Name: ")
    student.house = input('House: ')
    return student

if __name__ == "__main__":
    main()