number = int(input("Type the first number: "))
number1 = int(input("Type the second one: "))
if number > number1:
    print(f"First one is greater ({number}>{number1})")
elif number == number1:
    print(f"these are equal ({number}={number1})")
elif number < number1:
    print(f"Second one is greater ({number}<{number1})")   

