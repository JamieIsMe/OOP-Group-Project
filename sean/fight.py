import random
import math
import time


class User:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.coins = 0
        self.inventory = []
        self.dodge_chance = 0.3
        self.dodge_counter = 0

    def attack(self):
        base_damage = random.randint(10, 20)
        critical_chance = random.random()

        if critical_chance < 0.2:  # 20% chance for a critical hit
            print("Critical hit!")
            return math.ceil(base_damage * 1.5)
        else:
            return base_damage

    def dodge(self):
        if random.random() < self.dodge_chance:
            self.dodge_counter += 1
            return True
        return False

    def special_ability(self):
        if self.dodge_counter >= 3:
            print("You use your special ability!")
            special_damage = random.randint(15, 30)
            self.dodge_counter = 0
            return special_damage
        else:
            print("You can't use your special ability yet. Dodge "
                  "successfully three times first.")
            return 0


class RedCloakEnemy:
    def __init__(self):
        self.health = 80


def fight(user, enemy):
    print(f"The mysterious figure in the red cloak readys himself!")
    time.sleep(1)
    print("Prepare for battle!")

    while user.health > 0 and enemy.health > 0:
        print(f"\n{user.name}'s Health: {user.health} | "
              f"Red Cloak's Health: {enemy.health}\n")
        action = input("What will you do? (1. Attack, 2. Special Ability, "
                       "3. Attempt to flee): ")

        if action == "1":
            user_damage = user.attack()
            enemy.health -= user_damage
            print(f"You attack the Red Cloak and deal {user_damage} damage!")

            if user.dodge():
                print("The Red Cloak attacks, but you dodge the incoming "
                      "attack!")
            else:
                if enemy.health >= 0:
                    enemy_damage = random.randint(5, 15)
                    user.health -= enemy_damage
                    print(f"The Red Cloak counterattacks and deals "
                          f"{enemy_damage} damage to you!")
                else:
                    print("You have defeated the enemy")

        elif action == "2":
            special_damage = user.special_ability()
            if special_damage > 0:
                enemy.health -= special_damage
                print(f"You deal {special_damage} damage with your special "
                      f"ability.")

            if user.dodge():
                print("The Red Cloak attacks, but you dodge the incoming "
                      "attack!")
            else:
                if enemy.health >= 0:
                    enemy_damage = random.randint(5, 15)
                    user.health -= enemy_damage
                    print(f"The Red Cloak counterattacks and deals "
                          f"{enemy_damage} damage to you!")
                else:
                    print("You have defeated the enemy")

        elif action == "3":
            flee_chance = random.random()
            if flee_chance < 0.8:
                print("You managed to flee successfully!")
                return False
            else:
                print("You failed to flee. The Red Cloak catches up to you!")

        else:
            print("Invalid choice. Try again.")

        time.sleep(1)

    if user.health <= 0:
        print("You were defeated by the Red Cloak. Game over.")
        return None
    else:
        print("You defeated the Red Cloak! You gain a dagger and 25 coins.")
        return "Prized Dagger"


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = User(player_name)
    red_cloak = RedCloakEnemy()
    fight(player, red_cloak)
