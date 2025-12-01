total = 0
my_flag = True
number1 = 0
even = 0
odd = 0


while my_flag:
    number = int(input("please enter a number: "))
     
    if number == 0: 
        my_flag = False
        mean = number1 / total
        print(f"Total Number: {total}")
        print(f"Sum: {number1}")
        print(f"Mean: {mean}")
        print(f"Odd: {odd} Even: {even}")
    else:
        number1 = number + number1
        total = total + 1
        if number % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
            
print("bitti amk")