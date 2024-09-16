counter7: int = 0
num: int = int(input("Enter number :"))
while num % 7 == 0:
    counter7 += 1
    num: int = int(input ("Enter number :"))

    if num % 11 == 0:
        break
else:
    print(f"The count of numbers which divided with 7 is : {counter7}")

