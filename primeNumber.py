num = int(input("enter the number: "))
flag = 0
if num > 1:
    for i in range(2, num):
        if num % 2 == 0:
            flag = 1
            break

if flag == 1:
    print("given number is not a prime number")
else:
    print("given number is prime number")