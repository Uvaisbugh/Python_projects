import random

def roll_dice():
    """
    Simulates rolling two dice and displays their visual representation.
    """
    # Dice visual representations for each face.
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }

    # Ask the user if they want to roll the dice.
    roll = input("Roll the dice? (Yes/No): ").strip().lower()
    while roll == "yes":
        # Generate random numbers for the two dice.
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        # Display the results of the dice rolls.
        print(f"\nDice rolled: {dice1} and {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        # Ask the user if they want to roll again.
        roll = input("\nRoll again? (Yes/No): ").strip().lower()

    # End message when the user decides to stop rolling.
    print("Thanks for playing!")

# Run the dice rolling function.
roll_dice()
