
print("What is your name?")

name = input()

name = name.strip()

#It Will Remove White Spaces in between them

print(f"hello,{name}")

name = name.capitalize()

#It Will Capitalize the first Letter of the first Word

print("This is the Capitalized method",name)

name = name.title()

print("This is the the Title Method",name)



'''
this program can be written in this format also

name = input("Enter your name!").strip().title()

print("hello",name)

'''