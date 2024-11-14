#Here We are Using new file called CSV(comma seperated value)

with open("names5.csv") as file:
    for line in file:
        name,house =line.rstrip().split(",")
        print(f"{name} is in {house}")