
#a. Write a program to perform the following:
#i.  receive the full name, age and location from a user.
#ii. print out a description message to the user using f strings. The mesage should look like this:
   # Hello <full name>
   # I see you are <age> years old and you reside in <location>
    #NOTE: the full name should be in lower case (use string method)


full_name = input("enter your full name: ")
age = input("enter your age: ")
location = input("enter your location: ")
output = f"Hello {full_name.lower()}\ni see your are{age}years old\nand you reside in {location}"
print(output)



#b. Write a program that will take request for a user's name and then print the following:
# i. the complete name
#ii. the length of the name
#iii. the last character of the name

user_name = input("enter user name: ")
print(len(user_name))
print(user_name[-1])

