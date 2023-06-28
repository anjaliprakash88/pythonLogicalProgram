x = int(input("enter a number: "))
fact = 1
if x < 0:
    print("the number does not exist factorial")
elif x == 0:
    print("zero does not exist factorial")
else:
    for i in range(1, x + 1):
        fact = fact * i
    print("factorial of the given number is", fact)


# using Recursion

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


num = int(input("enter the number: "))
result = fact(num)
print("The Factorial of a given number is", result)
