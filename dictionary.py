

# menu = {
#     'morning': "Bread and Tea",
#     'post_morning': "Ginger Tea",
#     'afternoon': "Rice and Ege",
#     'evening': 'spaghetti'
# }

# v = list(enumerate(menu))


# for i, j in v:
#     print(f"index {i}: key: {")

#menu.get('morning')
#print(menu['morning'])
#print()


# dinner_type = input("what meal do you want to eat: ")
# meal = menu[dinner_type]
# meal = menu.get(dinner_type)
# if meal == none:
#     print(f"we dont have a meal for (dinner_type) time")
# else:
#     print(f"your (dinner_type) meal is meal")

# menu.pop('evening')

# print(menu)

# b= -90
# print(type(b))

# b = bool(b)
#print(type(b))



#print(b)

# def greeting(name):
#     print(f"hello {name}")


# greeting("Gideon")

# mysqr lambda x: x**2

# print(mysqr(4))




fruits = ['melon', 'apple', 'orange', 'mango']

newfruit = input('enter a new fruit to be added to the list: ')
fruits.append(newfruit)
print(fruits)

fruit_remove = input('enter a fruit you want to remove: ')
fruits.remove(fruit_remove)
print(fruits)

fruits.reverse()

print(fruits)

fruits = fruits.sort(reverse=True)
print(fruits)
