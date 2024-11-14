name = input("What is Your name? ")

file = open("name.txt","a")

file.write(name)

file.close()

"""
Here we created another bug here I executed the program 4 times so each time I had given various names
1)Harry
2)Hermoine
3)Teja
4)Ron
The Output is "HarryHermoineTejaRon"
"""