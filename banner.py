text = input("what is the text to display: ")
text_len = len(text)
space_count = text_len + 8
print("+" + space_count * "-" + "+")
print("|" + space_count * " " + "|")
print("|" + 4 * " " + text + 4 * " " + "|")
print("|" + space_count * " " + "|")
print("+" + space_count * "-" + "+")

