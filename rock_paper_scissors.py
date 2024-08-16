import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    computer_choice = get_computer_choice()
    player_choice = get_player_choice()

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    play_game()
