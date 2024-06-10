import random

def roll_dice():
    return random.randint(1, 6)

def take_turn(player_name, current_score, turn_score):
    while True:
        choice = input(f"\n{player_name}, \nroll (r) or hold (h)? ").lower()
        if choice == 'r':
            dice_roll = roll_dice()
            print(f"You rolled a {dice_roll}.")
            if dice_roll == 1:
                print("Pigged out! Turn score lost.")
                turn_score = 0
                break
            else:
                turn_score += dice_roll
                print(f"Turn score: {turn_score}")
        elif choice == 'h':
            current_score += turn_score
            print(f"{player_name}'s total score: {current_score}")
            break
        else:
            print("Invalid choice. Please enter 'r' or 'h'.")
    return current_score, turn_score

def play_game():

    num_players = int(input("Enter the number of players (up to 4): "))
    while num_players > 4 or num_players < 1:
        num_players = int(input("Invalid number of players. Please enter 1 to 4: "))

    player_names = []
    for i in range(num_players):
        player_names.append(input(f"Enter player {i+1}'s name: "))

    player_scores = {name: 0 for name in player_names}

    while True:
        for player_name in player_names:
            current_score = player_scores[player_name]
            turn_score = 0

            current_score, turn_score = take_turn(player_name, current_score, turn_score)
            player_scores[player_name] = current_score

            if current_score >= 50:
                print(f"{player_name} wins!")
                return

if __name__ == "__main__":
    print("Welcome to 6-PIG!")
    play_game()
