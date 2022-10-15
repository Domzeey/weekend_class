name = input('enter your name: ')
score = int(input('enter your score: '))

if score>=70 and score<=100:
    print(f"Hello {name}, your score is A")
elif score>=60 and score<=69:
    print(f"Hello {name}, your score is B")
elif score>=50 and score<=59:
    print(f"Hello {name}, your score is C")
elif score>=40 and score<=49:
    print(f"Hello {name}, your score is D")
elif score>=0 and score<=39:
    print(f"Hello {name}, your score is F")
else:
    print('invalid score')