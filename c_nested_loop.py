num: int = int(input("Plese provide number :"))
for x in range(num):
    print()
    for i in range(1, x + 2):
        print(i, end=" ")

for x in range(num):
    print()
    for i in range(1, num - x):
        print(i, end=" ")
