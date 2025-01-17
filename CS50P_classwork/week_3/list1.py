"""
This code is written 17th April 2024 @12:07
"""
students =["Harry","Teja","Hermione","Ron","Draco"]

#This will print the Entire list as a list
print(students)
#If we want to access the only one student we should use the Index Value

print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4]) #print(students[5]) when we use this it will give IndexError

#We can use for loop for the students

print("Printing Using Loop...")

for student in students:
    print(student)