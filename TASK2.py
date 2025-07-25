import random

# Available choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!\nChoose one: rock, paper, or scissors")
for i in range(1,4,1):
# Get user's choice
 user_choice = input("Your choice: ").lower()

# Get computer's choice
 computer_choice = random.choice(choices)

# Show both choices
 print(f"\nYou chose: {user_choice}")
 print(f"Computer choose: {computer_choice}")

# Decide the winner
 if user_choice == computer_choice:
    print("It's a tie!\n")
 elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! Rock beats scissors.\n")
    else:
        print("You lose! Paper beats rock.\n")
 elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! Paper beats rock.\n")
    else:
        print("You lose! Scissors beats paper.\n")
 elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Scissors beats paper.\n")
    else:
        print("You lose! Rock beats scissors.\n")
 else:
    print("Invalid input. Please choose rock, paper, or scissors.\n")
