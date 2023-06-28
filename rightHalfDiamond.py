row = int(input("enter the number of row: "))
for i in range(0, row):
    for j in range(0, i+1):
        print("* ", end=" ")
    print()
for i in range(1, row):
    for j in range(i, row):
        print("* ", end=" ")
    print()

