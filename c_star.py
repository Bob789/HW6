x = int(input("Enter a number: "))

for y in range(1, x+1, 2):
    print(" " * ((x - y) // 2) + "*" * y)
