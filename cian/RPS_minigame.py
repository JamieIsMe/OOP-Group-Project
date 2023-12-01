
import random


def Rock_Paper_Scissors_Game(player):

    bet = int(input(f"You have {player.coins} \nmany coins would you like to bet:\n"))

    while bet > player.coins:
        bet = int(input(f"You only have {player.coins} \nmany coins would you like to bet:\n"))

    player.coins = player.coins-bet

    choice = input("1) Rock\n2) Paper\n3) Scissors\n")
    player_choice = ""
    opponent_choice = ""

    if choice == "1":
        player_choice = "Rock"
    elif choice == "2":
        player_choice = "Paper"
    elif choice == "3":
        player_choice = "Scissors"

    choice = random.randint(1, 3)

    if choice == 1:
        opponent_choice = "Rock"
    elif choice == 2:
        opponent_choice = "Paper"
    elif choice == 3:
        opponent_choice = "Scissors"

    print("\nYour Choice:", player_choice)

    print("\nOpponents Choice:", opponent_choice, "\n")

    if player_choice == opponent_choice:
        print(f"Both players selected {opponent_choice}. It's a tie!")
        Rock_Paper_Scissors_Game()


    elif player_choice == "Rock":
        if opponent_choice == "scissors":
            print("Rock smashes scissors! You win!")
            bet = int(bet) * 2
            print("You get", bet, "coins")
        else:
            print("Paper covers rock! You lose.")
            bet = 0

    elif player_choice == "Paper":
        if opponent_choice == "Rock":
            print("Paper covers rock! You win!")
            bet = int(bet) * 2
            print("You get", bet, "coins")
        else:
            print("Scissors cuts paper! You lose.")
            bet = 0

    elif player_choice == "scissors":
        if opponent_choice == "Paper":
            print("Scissors cuts paper! You win!")
            bet = int(bet) * 2
            print("You get", bet, "coins")
        else:
            print("Rock smashes scissors! You lose.")
            bet = 0

    player.coins = player.coins + bet
    return



if __name__ == "__main__":
    Rock_Paper_Scissors_Game()