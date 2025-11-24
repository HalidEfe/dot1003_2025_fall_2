times = int(input("How many times a week do you eat at the student cafeteria? "))
price = int(input("The price of a typical student lunch? "))
money = int(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {times / 7 * price + money / 7}")
print(f"Weekly: {times * price + money}")
print(f"Monthly: {(times / 7 * price + money / 7) * 30}")