height = int(input(">Spruce height: "))

print(">")
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(f">{spaces}{stars}")
spaces2 = " " * (height - 1)
print(f">{spaces2}*")