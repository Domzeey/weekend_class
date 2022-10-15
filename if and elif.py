username = "yetunde2022"
password = '12345678'

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print(f"Hello {input_username}, Login Successfull")
elif input_username == username and input_password != password:
    print("incurrect password")
elif input_username != username and input_password == password:
    print("incurrect username")
else:
    print("invalid username or password")