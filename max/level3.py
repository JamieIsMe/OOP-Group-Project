"""
Program Name: level3.py

Author: Max Ceban

Program Description:

This is the third level out of our six-level game.
This level will mess with the player/Red Herring.
This is set in the middle of the town in which the player will need to solve riddles by npcs.
The clues collected throughout the level will lead to a plot twist in our player's quest.
The player can react with the merchants and can buy items that can enhance gameplay.
The player collects points based on key actions they committed.
Potential secret achievement? (Discuss it with the boys for that one.)

Date: 25/11/2023
"""

from sean.locationClass import Location
from cian.characters import NPC


class Level3(Location):
    """
    This class is the main function of our level three class
    """

    def __init__(self, score, coins):
        super().__init__("Town Center", ["Market", "Port", "Tavern"],
                         ["Textile Merchant", "BlackSmith", "Potion Mixer", "Street Performers",
                          "Tavern keeper"], ["Find someone in the tavern"])

        self.current_location = "entrance to the market"
        self.score = score  # Points depending on the player action in previous level
        self.coins = coins
        self.visted_locations = []
        self.blacksmith = NPC("Astrid Steelheart",
                              "Welcome to the Iron-heart Forge. What brings you here today adventurer? "
                              "\nNew armor, maybe new tools or a legendary sword for you?",
                              "Seen some cloaked folks gone to the potion mixer for some potions.", "Sword")

        # Boolean Variables set for no double interaction between any npcs
        self.__blacksmith_interacted = False

    def market(self):
        print(f"(Player Name) steps afoot to the {level3.location} of (Town name) lively {self.current_location}"
              f"square after (Ending of level 2),\n"
              f"where colourful stalls filled with treasure, the savory wonderful scent of roasting meats, "
              f"\nwith mesmerising street performances happening at the minute with camaraderie underneath the cold "
              f"snowy night.")

        while self.current_location == "entrance to the market":
            action = input("\nWhat will you do?,\n"
                           "1) Take a look around the market\n"
                           "2) Go to the tavern\n"
                           "3) Go to the Port\n")
            if action == "1":
                print("You decide to take a look around the market square it lays a symphony of sights, sounds, and "
                      "scent before you. You are mesmerised by the selection of medieval marvels.\n")
                print("A muscular blacksmith with a forge, wearing glittering sets of armour and superbly "
                      "manufactured weapons.\n")
                print("A lively stand decked out in finely woven textiles, selling anything from sumptuous silks to "
                      "long-lasting woollens.\n")
                print("On the other side we see a mysterious figure with cauldrons create magical concoctions ready to"
                      "bewitch anyone.\n")
                print("In the centre of the marketplace though not traditional merchants, \nthese street performers "
                      "add a dynamic element to this marketplace through their skills entertaining a crowd of people")

                character = int(input("\nWho do you want to interact with:\n"
                                      "1) Blacksmith\n"
                                      "2) Textile Merchant\n"
                                      "3) Potion Mixer\n"
                                      "4) See the street performers\n"))
                if character == 1:
                    if not self.__blacksmith_interacted:
                        print(self.blacksmith.interact())  # BLACKSMITH SPEAKS VOICE-LINE

                        while not self.__blacksmith_interacted:
                            interaction = int(input("1.) Ask about questions about the cult\n"
                                                    "2.) Ask about forging a sword\n"
                                                    "3.) Leave the blacksmith\n"))
                            # Checks if the user has found the clue already
                            # Else tell the user that you have the clue already
                            if interaction == 1:
                                print("(Player Name): Have you heard about the (Cult name) around abducting people "
                                      "recently.")
                                print(f"{self.blacksmith.name}: Yeah the market have been talking about the news.")
                                print(f"{self.blacksmith.name}: One of the merchants reported that they have went to "
                                      f"the potion mixer as of recently.")
                                # ADD CLUE ABOUT OBSERVATION
                            elif interaction == 2:
                                print(f"{self.blacksmith.name}: Ohh you interested in crafting an fine piece metal then"
                                      "you have to pay for it, it'll be 100 coins please.")
                                # An extra option depending on the score of the player
                                action = input(f"Want to purchase a sword for 100 coins?\n"
                                               "Yes\n"
                                               "No\n")
                                if action.lower() == "yes":
                                    if self.coins >= 100:
                                        print(f"{self.blacksmith.name}: Here your new sword wanderer, you must name "
                                              f"your sword for your future battle.\n")
                                        name_of_sword = input("Name your sword: ")
                                        self.blacksmith.item = name_of_sword
                                        # Add the name of sword to your inventory
                                    else:
                                        print(f"{self.blacksmith.name}: You don't have enough coins for the sword")
                                        # IF YOUR SCORE IS GOOD, SHE WILL GIVE IT FOR A DISCOUNT OR FREE
                                elif action.lower() == "no":
                                    pass
                                else:
                                    print("Invalid option")
                            elif interaction == 3:
                                print(f"{self.blacksmith.name}: I wish the best of luck in your future journey.")
                                self.__blacksmith_interacted = True
                    else:
                        print(f"You already interacted with {self.blacksmith.name}")

            elif action == "2":
                self.current_location = "Crown and Chalice Inn"
                print(f"You decide to head to the {self.current_location} "
                      f"hoping to find the clues to continue your quest.\n"
                      f"As you open the tavern door you see that's it filled with life as the melody playing"
                      f"\nLaughter echoed off the wooden wall with such a song of a drinking making the patrons "
                      f"stomping their feet in unison")
            elif action == "3":
                self.current_location = "Haven's Harbor"
                print("Welcome to Haven's Harbour, a medieval harbour full of marine legends and lively commerce.\n"
                      "Sturdy ships with aged sails dock next to cobblestone alleys where merchants peddle strange "
                      "items.")


if __name__ == "__main__":
    level3 = Level3(1, 100)
    level3.market()
