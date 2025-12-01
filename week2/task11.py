number = int(input("Please type in a temperature (F): "))
number1 = (number - 32) / 1.8
print(f"{number} degrees Fahrenheit equals {number1} degrees Celsius")

if number1 < 0:
    print("Brr! It's cold in here!")