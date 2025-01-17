#In this lets try to Sort there names 
names =[]
with open("names4.txt") as file:   #By default it will take read method
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")