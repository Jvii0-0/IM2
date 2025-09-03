while(True):

    row = int(input("Enter Row: "))
    col = int(input("Enter Column: "))
    search = int(input("Enter Search: "))

    if row <=0 or col <= 0:
        print("The system is ended!")
        break

    for x in range(1, row+1):
        for y in range(1, col + 1):
            if(search == x*y):
                print(f"[{x*y}]",end = " ")
            else:
                print(x*y, end = " ")
        print()