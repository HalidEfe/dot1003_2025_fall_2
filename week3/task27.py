password = input("Enter your password: ")

my_flag = True

while my_flag:
    againpassword = input("Enter again: ")
    if againpassword != password:
        print("They are not same.")
    else:
        print("Your password matches and account created successfully")
        my_flag = False

