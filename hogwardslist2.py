"""
We can use for loop

"""
students = ["Hermione","Harry","Teja","Roy"]

for i in students:
    print(i)

"""
Here we cannot pass range(student) because range is a 
integer and student in not an integer it is a list...
"""
#But We can use this method

for i in range(len(students)):
    print(i+1,students[i])

#I was printing there Index values also ,so Top most students
#names will print with respect to index values and we are adding 1

        

