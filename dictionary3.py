#'None' is a special keyword which variable doesn't have value at all
students = [
    {"name":"Hermoine","house":"Gryffindor","patronus":"Otter"},
    {"name":"Teja","house":"Gryffindor","patronus":"Dragon"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]
for student in students:
    print(student["name"])  
#This will print there name

for student in students:
    print(student["name"],student["house"],sep=", ")
#This will print names with respective houses

for student in students:
    print(student["name"],student["house"], student["patronus"])  
#This will print names with respective houses  and also patronous  
