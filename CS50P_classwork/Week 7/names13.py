students =[]

with open("names5.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        students.append(f"{name} is in {house}")
    
for student in sorted(students):
    print(student)

#We sorted whole CSF file by names