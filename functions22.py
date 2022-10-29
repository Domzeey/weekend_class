def match(x):
    return x+50
x = match(40)
print(x)


def me(*names):
    print("hello" + ' ' + names[1])
me("dominion","solomon","sunday")

def func_two(fruit1,fruit2):
    print("my favourite is"+" "+fruit2)
func_two(fruit1="cherry",fruit2="apple")


def func_three(**country):
    print(country["east"]+" "+"is a country in africa")
func_three(south = "south africa", east = "kenya")


def my_car(car="BMW"):
    print("my car is a"+" "+car)
my_car()

