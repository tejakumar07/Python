"""
This is update ProtoType for Grade

"""

score = int(input("Score: "))

if 100 <= score >= 90 :
    print("Grade: A")

elif 90 <= score >= 80 :
    print("Grade: B") 

elif 80 <= score >= 70 :
    print("Grade:C")

elif 70 <= score >= 60 :
    print("Grade: D")
elif 60 <= score >= 50 :
    print("Grade: E") 

else:
    print("Grade: F")