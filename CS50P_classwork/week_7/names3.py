name = input("What is your name?")

file = open("names1.txt","a")

file.write(f"{name}\n")

file.close()