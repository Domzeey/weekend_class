# write a program that will save the names of students in a text file.
# option one should be to add students and
#  option 2 to displayall students in text file
# option 3 empty the textfile.
# option 4 to end the program
# the program should use while loop so the program runs repeatedly




while True:
    print("enter 1 to add student name")
    print("enter 2 to display all students name")
    print("enter 3 to empty the textfile")
    print("enter 4 to end th program")
    choice = int(input("enter your choice: "))
    if choice == 1:
        file = open('students.txt', 'a')
        student_name = input("what is the student name: ")
        student_name += '\n'
        file.write(student_name)

    elif choice == 2:
        file = open('students.txt', 'r')
        lines = file.readlines()
        students_list = []
        for student in lines:
            student = student.rstrip()
            students_list.append(student)
        print(students_list)

    elif choice == 3:
        file = open('students.txt', 'w')
        file.write('')
        file.close
        
    

    elif chioce == 4:
        break    


