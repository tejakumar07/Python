while True:
    score = int(input("What's Score?"))

    if score >100:
        continue
    else:
        break


if 100 >= score >=90 :
    print("Your Grade is A")

elif 90 >= score > 80 :
    print("Your Grade is B")
elif 80 >= score > 70 :
    print("Your Grade is C")
elif 70 >= score > 60 :
    print("Your Grade is D")
elif 60 >= score > 50:
    print("Your Grade is E")
else:
    print("Your Grade is F")