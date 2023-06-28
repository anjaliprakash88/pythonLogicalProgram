# inverted half pyramid using  number
row = int(input("enter thr number of rows: "))
k = 0
for i in range(row, 0, -1):
    for j in range(i, 0, -1):
        print(i, end=" ")
        k = k + 1
    k = 0
    print("\n")

