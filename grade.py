score = int(input("Score: "))

if score <= 100 and score >= 90 :
    print("Grade: A")

elif score <90 and score > 80 :
    print("Grade: B") 

elif score < 80 and score > 70 :
    print("Grade:C")

elif score < 70 and score > 60 :
    print("Grade: D")
elif score < 60 and score > 50 :
    print("Grade: E") 

else:
    print("Grade: F")