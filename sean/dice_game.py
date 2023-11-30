import random
from denis.Player import Player

player = Player("Steve")


def roll_dice():
    print("Welcome to Roll the Dice!")

    player_wins = 0
    red_cloak_wins = 0

    while player_wins < 3 and red_cloak_wins < 3:
        input("Press Enter to roll the dice...")

        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        total = dice_1 + dice_2

        print(f"You rolled: {dice_1} and {dice_2}")
        print(f"Total: {total}")

        guess = input("Do you think the next roll will be 'higher' or "
                      "'lower'? ").lower()

        new_dice_1 = random.randint(1, 6)
        new_dice_2 = random.randint(1, 6)

        new_total = new_dice_1 + new_dice_2

        print(f"You rolled: {new_dice_1} and {new_dice_2}")
        print(f"Total: {new_total}")

        if (new_total > total and guess == 'higher') or (new_total <
                                                         total and guess ==
                                                         'lower'):
            print("Correct! You guessed right.")
            player_wins += 1
        else:
            print("Incorrect! Red cloak man wins this round.")
            red_cloak_wins += 1

        print(f"Your wins: {player_wins}, Red cloak man's wins:"
              f" {red_cloak_wins}")

    if player_wins == 3:
        print("Congratulations! You win! The man in the red cloak concedes "
              "defeat.")
        return "Prized Dagger"
    else:
        print("Game over! The man in the red cloak has defeated you.")
        return None


if __name__ == "__main__":
    roll_dice()
