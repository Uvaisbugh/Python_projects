#rock , papper, scissers game
import random

while True:
    print("rock, papper, scissers")
    print("Enter your choice: ")
    player_choice = input()
    if player_choice.lower() not in ["rock", "papper", "scissers"]:
        print("Invalid choice! Try again.")
        continue
    computer_choice = random.choice(["rock", "papper", "scissers"])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == "rock" and computer_choice == "scissers":
        print("You win!")
    elif player_choice == "papper" and computer_choice == "rock":
        print("You win!")  
    elif player_choice == "scissers" and computer_choice == "papper":
        print("You win!")
    else:
        print("You lose!")
    print(f"Computer choice: {computer_choice}")
    print("Do you want to play again? (yes/no)")
    play_again = input()
    if play_again.lower() != "yes":
        break  

print("Thanks for playing!")