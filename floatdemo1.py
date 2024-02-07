x = float(input("What is the Value of 'X'? "))

y = float(input("What is the value of 'Y'? "))

z= x+y

print("The Value of 'Z' is: ",z)

#According to the Documentation the round function is round(number[,ndigits]

print("The near value of 'Z' is",round(z))

#This will Give the value after the points(.) place 

a = round(z,1)

print(a)

#This F-String Method will Automatically seperate the values using comma(,) based on the number  System

print(f"This will F-String Method Method {z:,}")

e = x/y

print("The Division is",e)

