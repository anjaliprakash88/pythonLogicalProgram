vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
char = input("enter the alphabets to check vowels or consonants: ")
if char in vowels:
    print("given", char, "is vowels")
else:
    print("given", char, "is consonant")