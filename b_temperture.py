
x: int = int(0)
temperatures: float = 0
while x < 5:

    temperature: float = float(input("Plese provide temperature for city :"))
    if  -50 <=  temperature <= 45:
        temperatures += temperature
        x += 1
        print(f"You provide correct temperature :{x}")
else:
    print()
    evarage: float = float(temperatures / x)
    print(f"The Evrage temperature are : {evarage :.2f}")