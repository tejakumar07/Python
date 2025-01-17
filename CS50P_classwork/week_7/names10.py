#Let's Try make the lasst program more easy

with open("names4.txt") as file:

    for line in sorted(file):
        print(f"hello, {line.rstrip()}")

#In Last program we sorted names 
#But here We sorted entire file sorted
