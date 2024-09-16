import random

player1: str = str (input("Enter name of player1 :"))
player2: str = str (input("Enter name of player2 :"))
player3: str = str (input("Enter name of player3 :"))
player4: str = str (input("Enter name of player4 :"))

player: str = random.choice([player1, player2, player3, player4])
print(f" The winner of the lottery is : {player}" )