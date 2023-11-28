import time
from Puzzles import MedievalPuzzle
class Location:
    def __init__(self, location):
        self.location = location
        self.__investigated = False
        self.__inventory = []
        self._completedact = False

    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        if isinstance(value, bool):
            self.__investigated = value
        else:
            print("Investigated is expected to be a boolean.")

    def add_insight(self, insight):
        self.__inventory.append(insight)

    def view_inventory(self):
        print("Inventory:")
        for item in self.__inventory:
            print(f"- {item}")

    def investigate(self):
        if not self.investigated:
            print("You begin your journey!")
            print("You glance around the citadel, looking at the many portraits "
                  "on the walls")
            time.sleep(2)
            print("The portraits are of the 'Missing Six' - a group of people who "
                  "vanished mysteriously" )
            print("The portraits were smeared with a black ink-like substance?")
            time.sleep(4)
            print("Black Substance (Ink) - added to your inventory!")
            self.add_insight("Black Substance")
            time.sleep(2)
            print("The Druid, approaches...")

            # Add logic for investigation
            self.investigated = True
        else:
            print("You've already explored this location.")

class Game:
    def __init__(self):
        self.running = True
        self.game_started = False
        self.location = Location("Forgotten Citadel")
        self.player_name = ""

    def run(self):
        print("===================================")
        print("        Shadows of the            ")
        print("        Forgotten Realm             ")
        print("===================================")
        print("\nYou are about to embark on a quest veiled in the shadows.")
        print("Each level flows through the storyline, and you will be "
              "faced with puzzles"
              "\nand challenges!")
        print("Ready your weapons, gather your resolve and step into the unknown!")
        print("===================================")

        while self.running:
            self.update()

    def update(self):
        if not self.game_started:
            player_input = input("Press 's' to start or 'q' to quit: ")
            if player_input.lower() == 'q':
                self.running = False
            elif player_input.lower() == 's':
                self.game_started = True
                self.start_game()
        else:
            if not self.location.investigated:
                print("===================================")
                player_input = input("Press 'q' to quit, 'c' to continue, "
                                     "'i' to investigate the area :")
            else:
                print("===================================")
                player_input = input("Press 'q' to quit, 'c' to continue or 't' to view "
                                     "your inventory: ")

            if player_input.lower() == "q":
                self.running = False
            elif player_input.lower() == "c":
                self.act2()
            elif player_input.lower() == "t":
                self.location.view_inventory()
            elif (player_input.lower() == "i" and not
                    self.location.investigated):
                self.location.investigate()
            elif player_input.lower() == "i" and self.location.investigated:
                print("You've already explored this location.")

    def start_game(self):
        self.player_name = input("Enter your name to immerse yourself in the story: ")
        print(f"Welcome, Adventurer {self.player_name}!")
        print("Let's begin...")
        print("The Year: 476 AD")
        print("'Our story begins in the Forgotten Citadel'.")
        print("Follow the cues in the terminal and good luck!")

    def act2(self):
        act_completed = False
        print("(The Druid approaches you...)")
        user_input = input("Do you wish to speak to him? (y/n): ")
        if user_input.lower() == 'y':
            MedievalPuzzle()
        elif user_input.lower() == 'n':
            print("You must speak to the druid to continue the quest!")
        else:
            print("That is an invalid choice!")

    def continue_game(self):
        print("You delve deeper into the unknown...")

