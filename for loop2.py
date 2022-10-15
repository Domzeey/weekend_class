# students = ['dominion', 'yetunde', 'justice']

# {
#     'dominion': {
#         'matric_no': '09090',
#         'location': 'yaba'
#     },
#     'yetunde': {
#         'matric_no': '09090',
#         'location': 'yaba'
#     },
#     'justice': {
#         'matric_no': '09090',
#         'location': 'yaba'
#     }
# }

students = ['dominion', 'yetunde', 'justice']
dict_students = {}

for student in students:
    if student == 'justice':
        print("we will skip justice")
    else:
        print(f"current student is {student}")
        mat_no = input("enter matric number: ")
        location = input("enter location: ")

        dict_students[student] = {
        'matric no': mat_no,
        'location': location
    }
print(dict_students)