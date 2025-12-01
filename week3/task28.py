number = int(input("Please enter a number: "))

my_flag = True

while my_flag:
    print(number)
    number = number - 1
    if number == 0:
     my_flag = False
     print("Kaboom")
     