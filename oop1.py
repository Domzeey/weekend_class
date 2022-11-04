# class car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.price = year


# car_1 = car("Toyota", 2018)  #instantiate the car class 
# car_2 = car("Honda", 2022)   #another instance of the car class

# #access the class attributes
# print(car_1.brand)
# print(car_2.brand)





# class student:
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#     def profile(self):
#         return(f"Hi {self.name}, your course is {self.course} ")

# student_1 = student("Dominion","Accounting")
# student_2 = student("Solomon","Statistics")

# print(student_1.name)
# print(student_2.course)
# print(student_1.profile())




# employee_name = input("enter employee name: ")
# employee_salary = int(input("enter employee salary: "))

# def employee_info(employee_name,employee_salary=9000):
#     return(f"Hi {employee_name}, your salary is {employee_salary}")
# print(employee_info("Dominion",employee_salary))




# def show_employee(name,salary=9000):
#     return(f"Hi {name}, your salary is {salary}")
# print(show_employee("dominion"))


values = list(map(int,input('enter three numbers: ').split()))
output = []
def show_squares(values):
    for i in values:
        ans = i ** 2
        output.append(ans)
    return output

print(show_squares(values))


