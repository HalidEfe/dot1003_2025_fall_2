number = 3
password = 314159
my_flag = True

while my_flag:
    user_password = int(input("Password: "))
    number = number - 1 
    if password == user_password:
        my_flag = False
        print("Welcome")
    elif number == 0:
        my_flag = False
        print("Incorrect Password. Exterminate...")
    else:
        print("Try again")
    



