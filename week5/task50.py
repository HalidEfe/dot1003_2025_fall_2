string = input("Please enter string:")
element = input("Please enter search item:")

index = string.find(element)

if index != -1:
    print(f"found it at {index}")
else:
    print("not found")