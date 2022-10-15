#you have a list of students firstname stored in a list
#called student as shown below:

#students = ['dominion', 'yetunde', 'justice']


#write a program that will ask all the students in
#the list for their last name,
#and replace their first name in the list with the full name



# Hint: the full name is the combination of thei first and 
# last name





students = ['dominion', 'yetunde', 'justice']

for index, student_name in enumerate(students):
    print(f"current student is {student_name}")
    last_name = input("enter your last name: ")
    full_name = f"{last_name} {student_name}"
    students[index] = full_name

print(students)