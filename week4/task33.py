
my_flag = True
my_list = []


while my_flag:
    a = input("please enter an input")

    
    if a == "exit":
        print(my_list)
        my_flag = False
    else:
        my_list.append(a)


       
