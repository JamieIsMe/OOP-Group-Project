
import random


def dice_game(player):

    bet = int(input(f"You have {player.coins} \nmany coins would you like to bet:\n"))

    while bet > player.coins:
        bet = int(input(f"You only have {player.coins} \nmany coins would you like to bet:\n"))

    player.coins = player.coins-bet

    player_dice1 = random.randint(1, 6)
    player_dice2 = random.randint(1, 6)
    total_player_dice = player_dice1 + player_dice2

    opponent_dice1 = random.randint(1, 6)
    opponent_dice2 = random.randint(1, 6)
    total_opponent_dice = opponent_dice1 + opponent_dice2

    print("\nYour Dice:")
    print("Dice 1:", [player_dice1], "\nDice 2:", [player_dice2], "\nTotal:", [total_player_dice])

    print("\nOpponents Dice:")
    print("Dice 1:", [opponent_dice1], "\nDice 2:", [opponent_dice2], "\nTotal:", [total_opponent_dice])

    if total_player_dice > total_opponent_dice:
        print("\nYou Win")
        bet = int(bet) * 2
        print("You get", bet, "coins")

    elif total_player_dice == total_opponent_dice:
        print("\nDraw!\nGo Again")
        dice_game()

    else:
        print("\nYou Lost")
        bet = 0
    player.coins = player.coins + bet
    return


if __name__ == "__main__":
    dice_game()