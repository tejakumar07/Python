names =[] #Creating a empty list and then we will append names to the list

for _ in range(5):
    names.append(input("What is Your name?")) #It will saves the names in the list

for name in sorted(names):
    print(f"hello, {name}") #here the sort method will automatically arrange there names in alphabetical order