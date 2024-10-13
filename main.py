import random

# Available options
com_opt = ["Rock", "Paper", "Scissor"]
comdict = {"Rock": 1, "Paper": -1, "Scissor": 0}
youdict = {"r": 1, "p": -1, "s": 0}

# Function to check the result
def check_winner(user_choice, com_choice):
    if user_choice == com_choice:
        return "It's a tie!"
    elif (user_choice - com_choice) % 3 == 1:
        return "You win!"
    else:
        return "You lose!"

# Main game loop
while True:
    # Get the computer's choice
    com_sel = random.choice(com_opt)
    uchoice = input("Enter your choice,\n R for Rock \n P for Paper \n S for Scissor\n").lower()

    # Check for valid input
    if uchoice not in youdict:
        print("Invalid input. Please try again!")
        continue

    # Convert choices to comparable format
    user_option = youdict[uchoice]
    com_option = comdict[com_sel]

    # Determine the winner
    result = check_winner(user_option, com_option)
    
    # Display the result
    print(f"You chose {uchoice.upper()} and Computer chose {com_sel}. {result}")

    # Ask the user to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
