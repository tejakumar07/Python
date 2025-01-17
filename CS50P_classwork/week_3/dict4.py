students = [
    { "name":"Hermione","house":"Gryffindor","patronous":"Otter"},
    {"name":"Teja","house":"Gryffindor","patronous":"Dragon"},
    {"name":"Harry","house":"Gryffindor","patronous":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronous":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronous":None},

]

#Here We used A speacial Keyword called 'None' for Draco since he Doesnt had any Any Pen In the Hogwards World


for student in students:
    print(student["name"]) #This will print Names
    print(student["name"],student["house"]) #This will print there names and houses
    print(student["patronous"]) #This will print there Patronous