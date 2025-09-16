mydict = {}

mydictSize = int(input("Matrix size: "))
for i in range(mydictSize):
    val = input(f"Shopping items{i+1}: ")
    mydict[i] = val

print(f"\nYou have {len(mydict)} items in the cart\n")

while True:
    userInput = input("What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").strip()

    if userInput == '*':
        print("Bye")
        break

    elif userInput.lower() == 'd':
        print("Displaying Values")
        print(f"{'Key':<8}{'Value'}")
        for k, v in mydict.items():
            print(f"{k:<8}{v}")

    elif userInput.lower() == 's':
        search_input = input("Enter key or item to search: ").strip()
        try:
            key_search = int(search_input)
            val = mydict.get(key_search)
            if val is not None:
                print(f"Found {val} item")
            else:
                print("I'm sorry, not in the cart")
        except ValueError:
            found = False
            for key, val in mydict.items():
                if val.lower() == search_input.lower():
                    print(f"Found {val} item")
                    found = True
                    break
            if not found:
                print("I'm sorry, not in the cart")

    elif userInput.lower() == 'r':
        key_input = input("Enter key to search: ").strip()
        try:
            key_to_remove = int(key_input)
            removed_val = mydict.pop(key_to_remove, None)
            if removed_val is not None:
                print(f"The key {key_to_remove} with value {removed_val} has been deleted")
            else:
                print("Key not found")
        except ValueError:
            print("Key not found")

    elif userInput.lower() == 'c':
        key_input = input("Enter key to search: ").strip()
        try:
            key_to_change = int(key_input)
            current_val = mydict.get(key_to_change)
            if current_val is not None:
                print(f"Found {current_val} item")
                new_val = input("Enter value: ")
                mydict[key_to_change] = new_val
            else:
                print("I'm sorry, not in the cart")
        except ValueError:
            print("Key not found")

    else:
        print("Invalid option. Please choose C, R, D, S or * to exit.")
