year = input("enter year: ")
day = input("day(1-31): ")
month = ["january", "february", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
monthIndex = int(input("Enter month (1-12): ")) - 1
monthOutput = month[monthIndex]
endings = ["st", "nd", "rd"] + 17 * ["th"] + ["st", "nd", "rd"] + 7 * ["th"] + ["st"]
dayIndex = int(day) - 1
dayOutput = day + endings[dayIndex]
print(monthOutput + " " + dayOutput + " ," + year)
