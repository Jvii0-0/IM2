while True:
    row = int(input("Enter number of rows: "))
    col = int(input("Enter number of columns: "))
    search = int(input("Enter number to search: "))

    if row <= 0 or col <= 0:
        break

    for i in range(row + 1):
        for y in range(col + 1):
            if i * y != 0:
                if i * y == search:
                    print(f"[{i*y}]", end=" ")
                else:
                    print(f" {i*y}", end="  ")
            else:
                print("  ", end = "  ")
        print()