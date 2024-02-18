"""
students = ["Hermione","Teja","Harry","Roy","Draco"]
house = ["Gryffindor","Griffindor","Griffindor","Griffindor","Slytherin"]
"""
"""
we are matching the each stundent with each house like 
Hermione with Gryffindor and teja with Gryffindor and 
all list Index (0,0) matching student with the house
"""
students ={
    "Hermoine":"Gryffindor",
    "Teja":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
          }
print(students["Hermoine"])
print(students["Teja"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(students)
