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
        self.name = "Red Cloaked Enemy"
        self.health = 80


class CultMember:
    def __init__(self):
        self.name = "cult member"
        self.health = 100


def fight(user, enemy):
    print(f"The {enemy.name} readys himself!")
    time.sleep(1)
    print("Prepare for battle!")

    while user.health > 0 and enemy.health > 0:
        print(f"\n{user.name}'s Health: {user.health} | "
              f"{enemy.name}'s Health: {enemy.health}\n")
        action = input("What will you do? (1. Attack, 2. Special Ability, "
                       "3. Attempt to flee): ")

        if action == "1":
            user_damage = user.attack()
            enemy.health -= user_damage
            print(f"You attack the {enemy.name} and deal {user_damage} "
                  f"damage!")

            if user.dodge():
                print(f"The {enemy.name} attacks, but you dodge the incoming "
                      "attack!")
            else:
                if enemy.health >= 0:
                    enemy_damage = random.randint(5, 15)
                    user.health -= enemy_damage
                    print(f"The {enemy.name} counterattacks and deals "
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
                print(f"The {enemy.name} attacks, but you dodge the incoming "
                      "attack!")
            else:
                if enemy.health >= 0:
                    enemy_damage = random.randint(5, 15)
                    user.health -= enemy_damage
                    print(f"The {enemy.name} counterattacks and deals "
                          f"{enemy_damage} damage to you!")
                else:
                    print("You have defeated the enemy")

        elif action == "3":
            flee_chance = random.random()
            if flee_chance < 0.2:
                print("You managed to flee successfully!")
                return False
            else:
                print(f"You failed to flee. The {enemy.name} catches up to "
                      "you!")

        else:
            print("Invalid choice. Try again.")

        time.sleep(1)

    if user.health <= 0 and enemy.name == "Red Cloaked Enemy":
        print(f"You were defeated by the {enemy.name}. Game over. ☠️")
        return None
    elif user.health <= 0 and enemy.name == "cult member":
        print(f"You were defeated by the {enemy.name}. Game over. ☠️")
        return None
    elif enemy.name == "cult member":
        print(f"You defeated the {enemy.name}! "
              f"You gain a map that shows the location of the (CULT NAME) "
              f"home base and 200 coins. 🗺️")
        return "Map to cult homebase"
    else:
        print(f"You defeated the {enemy.name}! You gain a dagger and 25 "
              f"coins.")
        return "Prized Dagger"


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    player = User(player_name)
    red_cloak = RedCloakEnemy()
    cult_member = CultMember()
    fight(player, red_cloak)
    fight(player, cult_member)
