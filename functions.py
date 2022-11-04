# def fullname():
#     print('Dominion')

# fullname()


# def fullname(f_name,l_name):
#     print("your fullname is " + f_name +"," + l_name)

# fullname("dominion","solomon")



# f_name = input('enter first name: ')
# l_name = input('enter last name: ')

# def fullname(f_name,l_name):
#     print("your fullname is " + f_name +"," + l_name)

# fullname(f_name,l_name, "today")



# x = int(input('enter the value of x: '))
# y = int(input('enter the value of y: '))

# def xy(x,y):
#     print("th value of ", x * y)

# xy(x,y)






# def my_country(name="Nageria"):
#     print("i am from ", name)

# my_country("ghana")


# def my_country(name="Nageria"):
#     country = "i am from " + name
#     return country

# print(my_country("ghana"))




# x = list(map(int,input('enter three numbers: ').split()))

# def duplicate(x):
#     y = []
#     for value in x:
#         new = value * 2
#         y.append(new)
#     return y

# print(duplicate(x))





# write a function that returns the max number in x
#  x should be a list

# x = list(map(int,input('enter numbers: ').split()))

# def find_maximum(x):
#     ans = max(x)
#     return ans

# print(find_maximum(x))





#     # writa a function that returns the length of
#     # a string, the string should be a user input

# word = input('enter a word: ')

# def xx():
#     print(len(word))
# xx()
    



# x = list(map(int,input('enter numbers: ').split()))

# def find_minimum(x):
#     ans = min(x)
#     return ans

# print(find_minimum(x))



def outer_func():
    def inner_func():
        print("hello, world")
    inner_func()
outer_func()