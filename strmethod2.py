name =input("What is your Name?")

name = name.lstrip()

#Ramove spaces from left side

name = name.rstrip()

#Remove white spaces from Right Side

print("hello",name)

first , last = name.split(" ")

print(f"hello,{first}")



