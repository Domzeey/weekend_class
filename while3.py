fridge ={}

while True:
    print("enter 1 to add item\nEnter 2 to remove item")
    print("enter 3 to clear fridge\nEnter 4 to update item")
    print("enter 5 to print all item\nEnter 6 to end program")

    choice = int(input("enter your choice"))
    if choice ==1:
        item = input('what item do you want to add: ')
        quantity = int(input("Enter quantity: "))
        fridge[item] = quantity
        print(f'{item} added successfully')

    elif choice == 2:
        item = input("what item do you want to remove")
        fridge.pop(item)
        print(f"{item} has been removed successfully from list")

    elif choice == 3:
        fridge.clear()
        print("fridge has been emptied")

    elif choice == 4:
        item = input("what item do you want to add to: ")
        quantity = int(input("Enter quantity to add: "))
        fridge[item]+= quantity
        print(fridge)

    elif choice ==5:
        print(fridge)
    
    elif choice == 6:
        print(fridge)
        break
    else:
        break