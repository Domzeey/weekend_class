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