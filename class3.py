name = input('enter your name: ')
age = int(input('enter your age: '))

if age>=0 and age<=4:
    print(f"Hello {name}, you are still a baby")
elif age>=5 and age<=12:
    print(f"Hello {name}, you are a child")
elif age>=13 and age<=19:
    print(f"Hello {name}, you are a Teenager")
elif age>=20 and age<=50:
    print(f"Hello {name}, you are an Adult")
elif age>=51:
    print(f"Hello {name}, you are Elderly")
else:
    print('invalid age')














