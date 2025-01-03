import random

counter = 0
while True:
    choice = input("Let's Dice (y/n) : ").lower()
    if choice == "y":
        dice_c = int(input("how many dice you want ? : "))
        counter += 1
        print(f"this is {counter} time.")
        for n in range(1, dice_c + 1):
            dice = random.randint(1, 6)
            print(f"{dice}")
    elif choice == "n":
        quit_or = input("exit (y/n): ").lower()
        if quit_or == 'y':
            break
        elif quit_or == 'n':
            continue
        else:
            print("invalid !")
    else:
        print("invalid !")
