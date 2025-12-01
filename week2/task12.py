wage = float(input("Hourly wage: "))
work = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    print(wage * work * 2)
else:
    print(wage * work)
    