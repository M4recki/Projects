Dictionary = {}
while(True):
    print("--------------------------------------------------------------------------------------")
    print("Welcome to the dynamic dictionary program")
    print("1- Add new definition 2- Search existing definition 3- Delete given definition 4- Quit")
    Interface = input("Which option do you want to choose? ")
    if Interface=="1":
        Key = input("What key (word) would you like to define? ")
        Definition = input("What definition would you like to add? ")
        Dictionary[Key] = Definition
        print("Definition: ", Definition, "has been successfully added to the dictionary.")
    elif Interface=="2":
        Key = input("What definition are you looking for? ")
        if Key in Dictionary:
            print("Definition: ", Key, "is currently in the dictionary.")
        else:
            print("Definition: ", Key, "hasn't been found.")
    elif Interface=="3":
        Key = input("What definition would you like to delete? ")
        if Key in Dictionary:
            del Dictionary[Key]
            print("Definition: ", Key, "has been successfully removed from the dictionary.")
        else:
            print("Definition: ", Key, "hasn't been found.")
    elif Interface=="4":
        print("Thank you for using my service. :)")
        break
    else:
        print("Option: ", Interface, "doesn't exist. Please choose correct option from the list")
