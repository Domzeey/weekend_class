

#item_power = lambda x,y: x**y

# print(item_power(3,4))
# numbers = [2,4,6,8]
# deals = [1000, 3000, 6000, 2000]
# newlist = map(lambda x: x**2, numbers)
# my_share = map(lambda x: x * 0.25, deals)
# print(list(my_share))

score = [100, 70, 20, 40, 20, 90, 70, 54, 89]
a_list = filter(lambda x: x>=70, score)

print(list(a_list))



