import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)
length = int(input("Enter password length: "))
password = []
for i in range(length):
		password.append(random.choice(characters))
print("".join(password))


