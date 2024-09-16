from random import randint

number_target: int = randint(1, 100)
counter: int = 1
guess_number: int = int (input("Please guess a number :"))

while guess_number != number_target:
    counter += 1
    if guess_number > number_target:
        print("Your number is too big, Try agein")
    else:
        print("Your number is too small, Try agein")
    guess_number: int = int(input("Please guess a number :"))

else:
    print( "BINGO ")
    print(f"Your guess is : {counter}")