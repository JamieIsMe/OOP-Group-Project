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
from denis.Player import Player
from sean.locationClass import Location
from cian.characters import NPC
from minigame import cipher_decryption_game


class Level3(Location):
    """
    This class is the main function of our level three class
    """

    def __init__(self, score, coins):
        super().__init__("Town Center", ["Market", "Crown and Chalice Inn", "Haven's Port"],
                         ["Textile Merchant", "BlackSmith", "Potion Mixer", "Street Performers",
                          "Tavern keeper"], ["Find someone in the tavern"])

        self.user = Player("Max")
        self.current_location = self.sublocation[0]
        self.score = score  # Points depending on the player action in previous level
        self.coins = coins  # Coins collected throughout the game to aid the player in future quests

        self.blacksmith = NPC("Astrid Steelheart",
                              "Welcome to the Iron-heart Forge. What brings you here today adventurer? "
                              "\nNew armor, maybe new tools or a legendary sword for you?",
                              "Seen some cloaked folks gone to the potion mixer for some potions.", "Sword", "")

        self.textile_merchant = NPC("Elara Looming",
                                    "Dear patrons, welcome to the world of wonder!\n"
                                    "Step into the world of Velvet Haven Textiles, where every thread tells a story "
                                    "and every fabric whispers its unique story.", "Paper with the cult logo",
                                    "Fur coat", "")

        self.potion_mixer = NPC("Gwyneth Gerald",
                                f"Ah, hello, adventurer! Enter the mystical embrace of Gwyneth's sorcery.\n"
                                f"There, the air is filled with the enchanting essence of unknown possibilities.",
                                "Deciphered Message", "Spellbook", "")

        self.street_performer = NPC("The juggler",
                                    "Yeah, saw someone briefly, but they vanished into the crowd. Might "
                                    "be nothing", "Cloaked figure near fountain", " ", "")

        self.drunken_elf1 = NPC("Aricen Emberheart",
                                ["You know what's the best part about being an elf? We're like, "
                                 "timeless, man. I've got all the time in the world to enjoy "
                                 "this tavern!",
                                 "Tomorrow is just a distant future. I'm living in the present, "
                                 "and the present says, 'Another round!'",
                                 "I challenged a dwarf to an arm-wrestling match. Turns out, dwarves are surprisingly "
                                 "strong. Who knew?", "Gnomorin? That's a new elven name right there. Maybe he'll join "
                                                      "us on our timeless quest for more drinks!"], "", "",
                                ["Swaying on the stool"])

        self.drunken_elf2 = NPC("Clarista Starfall", ["Timeless? I think you've had too much elven wine, friend. "
                                                      "You've got tomorrow morning catching up with you.",
                                                      "Speaking of company, did you guys see the human bard trying to "
                                                      "serenade the barmaid? Hilarious!",
                                                      "You challenged a dwarf? "
                                                      "That's like challenging a mountain to a staring contest. "
                                                      "You're brave, or maybe just tipsy.",
                                                      "I'm in! To Gnomorin and the quest for another round!"], "", "",
                                ["Raising an eyebrow"])

        self.drunken_elf3 = NPC("Thandor Dawnwhisper",
                                ["Present, future, who cares? I'm just here for the company and the questionable "
                                 "decisions!",
                                 "Yeah, he sounded like a cat being strangled by a bagpipe. "
                                 "No offense to cats or bagpipes.",
                                 "I tried to teach a gnome some elven dance moves. "
                                 "Now he's convinced he's an honorary elf. Keeps "
                                 "calling himself 'Gnomorin.'", "To questionable decisions and unforgettable nights!"],
                                "", "", ["Joining the conversation", "laughing"])

        self.drunken_elves = [self.drunken_elf1, self.drunken_elf2, self.drunken_elf3]

        # Boolean Variables set for no double interaction between any npcs
        self.__blacksmith_interacted = False
        self.__textile_merchant_interacted = False
        self.__potion_mixer_interacted = False
        self.__street_performer_interacted = False

        print(f"{self.user.name} steps afoot to the town center of (Town name) lively {self.current_location}"
              f" square after (Ending of level 2),\n"
              f"where colourful stalls filled with treasure, the savory wonderful scent of roasting meats, "
              f"\nwith mesmerising street performances happening at the minute with camaraderie underneath the cold "
              f"snowy night.")

    def market(self):
        while self.current_location == "Market":
            action = input("\nWhat will you do?,\n"
                           "1) Take a look around the market\n"
                           "2) Go to the tavern\n"
                           "3) Go to the Port\n")
            if action == "1":
                if self.current_location not in self.visited_sublocations:
                    print("\nYou decide to take a look around the market square it lays a symphony of sights, sounds, "
                          "and scent before you. You are mesmerised by the selection of medieval marvels.\n")
                    print("A muscular blacksmith with a forge, wearing glittering sets of armour and superbly "
                          "manufactured weapons.\n")
                    print("A lively stand decked out in finely woven textiles, selling anything from sumptuous silks to"
                          "long-lasting woollens.\n")
                    print("On the other side we see a mysterious figure with cauldrons create magical concoctions "
                          "ready to bewitch anyone.\n")
                    print("In the centre of the marketplace though not traditional merchants, \nthese street performers"
                          "add a dynamic element to this marketplace through their skills entertaining a crowd of "
                          "people.")
                    Level3.market_square(self)
                else:
                    print("You already visted the market")
            elif action == "2":
                self.current_location = self.sublocation[1]
                Level3.tavern(self)
            elif action == "3":
                self.current_location = "Haven's Harbor"
                print("Welcome to Haven's Harbour, a medieval harbour full of marine legends and lively commerce.\n"
                      "Sturdy ships with aged sails dock next to cobblestone alleys where merchants peddle strange "
                      "items.")

    def market_square(self):
        character = int(input("\nWho do you want to interact with:\n"
                              "1) Blacksmith\n"
                              "2) Textile Merchant\n"
                              "3) Potion Mixer\n"
                              "4) See the street performers\n"
                              "5) Leave the market square.\n"))

        match character:
            case 1:
                print("\n")
                Level3.interact_with_blacksmith(self)
            case 2:
                print("\n")
                Level3.interact_with_textile_merchant(self)
            case 3:
                print("\n")
                Level3.interact_with_potion_mixer(self)
            case 4:
                print("\n")
                Level3.interact_with_street_performers(self)
            case 5:
                Level3.visited(self, self.current_location)
                Level3.market(self)
            case _:
                print("Invalid choice")

    def interact_with_blacksmith(self):
        if not self.__blacksmith_interacted:
            print(self.blacksmith.interact())  # BLACKSMITH SPEAKS VOICE-LINE

            while not self.__blacksmith_interacted:
                interaction = int(input(f"1.) Question {self.blacksmith.name} about the cult\n"
                                        f"2.) Ask about forging a sword\n"
                                        f"3.) Leave the blacksmith\n"))
                # Checks if the user has found the clue already
                # Else tell the user that you have the clue already
                if interaction == 1:
                    print(f"{self.user.name}: Have you heard about the (Cult name) around abducting people "
                          "recently.")
                    print(self.blacksmith.say_dialogue("Yeah the market have been talking about the news."))
                    print(self.blacksmith.say_dialogue("One of the merchants reported that they have went to "
                                                       f"the potion mixer as of recently."))
                    Level3.add_clue(self, "Blacksmith's observation on the potion mixer")
                elif interaction == 2:
                    if self.blacksmith.items not in self.user.inventory:
                        print(self.blacksmith.say_dialogue("Ohh you interested in crafting an fine piece metal then"
                                                           "you have to pay for it, it'll be 100 coins please."))
                        # An extra option depending on the score of the player
                        action = input(f"Want to purchase a sword for 100 coins?\n"
                                       "Yes: Y\n"
                                       "No: N\n")
                        if action.lower() == "y":
                            if self.coins >= 100:
                                print(self.blacksmith.say_dialogue("Here's your new sword wanderer, you must name "
                                                                   f"your sword for your future battle."))
                                self.coins = self.coins - 100
                                print(f"New balance: {self.coins}")
                                print(self.blacksmith.say_dialogue(f"The sword suits you traveler, this "
                                                                   f"will help you for sure"))
                                self.user.add_item(self.blacksmith.items)
                            else:
                                print(self.blacksmith.say_dialogue("You don't have enough coins for the sword."))
                                # IF YOUR SCORE IS GOOD, SHE WILL GIVE IT FOR A DISCOUNT OR FREE
                        elif action.lower() == "n":
                            pass
                        else:
                            print("Invalid option")
                    else:
                        print(self.blacksmith.say_dialogue("You have a sword already adventurer!"))
                elif interaction == 3:
                    print(self.blacksmith.say_dialogue("I wish the best of luck in your future journey."))
                    self.__blacksmith_interacted = True
        else:
            print(f"You already interacted with {self.blacksmith.name}")

        level3.market_square()

    def interact_with_textile_merchant(self):
        if not self.__textile_merchant_interacted:
            print(self.textile_merchant.interact())

            while not self.__textile_merchant_interacted:
                interaction = int(input(f"1.) Ask about the newest trends in the shop\n"
                                        f"2.) Question {self.textile_merchant.name}\n"
                                        f"3.) Leave the textile merchant\n"))
                # Checks if the user has found the clue already
                # Else tell the user that you have the clue already
                if interaction == 1:
                    if self.textile_merchant.items not in self.user.inventory:
                        print(self.textile_merchant.say_dialogue(
                            "Discover our collection of popular trends in intricate embroidery, sumptuous velvet, "
                            "and natural, earthy tones.\nYou can also expect shimmering metallic threads, breathable "
                            "linens, and gorgeous brocade fabrics, each fabric unique in its own way.\nIt tells a story"
                            " of elegance."))

                        action = input("You take a gander around the shop and seek upon a fur coat for 25 coins.\n"
                                       "Do you wish to purchase it?\n"
                                       "Yes: Y\n"
                                       "No : N\n")

                        if action.lower() == "y":
                            if self.coins >= 25:
                                print(self.textile_merchant.say_dialogue(f"I see the fur coat interests you, this is "
                                                                         f"yours now wanderer it might help in the "
                                                                         f"extreme weather conditions ahead of your "
                                                                         f"journey."))
                                self.user.add_item(self.textile_merchant.items)
                            else:
                                print(self.textile_merchant.say_dialogue("You do not have another coins for the fur "
                                                                         "coat,\nadventurer perhaps maybe you can find "
                                                                         "my missing cherished chicken Feather cluck, "
                                                                         "and my heart aches without its presence.\n"
                                                                         "I may provide a extra reward onto of this as "
                                                                         "well."))  # SIDE QUEST FOR THE LEVEL
                        elif action.lower() == "n":
                            pass
                        else:
                            print("Invalid option")
                    else:
                        print(self.textile_merchant.say_dialogue("You have a fur coat already adventurer!"))
                elif interaction == 2:
                    print(self.textile_merchant.say_dialogue("Oh yes those people, one of the members a few days \n"
                                                             "ago tried to influence me to join the cult and left me"
                                                             " this.\n"))
                    print(f"{self.textile_merchant.name} hands you a {self.textile_merchant.clues}")
                    Level3.add_clue(self, self.textile_merchant.clues)
                elif interaction == 3:
                    print(self.textile_merchant.perform_action("Waves nervously as I leave the stores maybe its just \n"
                                                               "his chicken is missing"))
                    self.__textile_merchant_interacted = True
        else:
            print(f"You already interacted with {self.textile_merchant.name}")

        level3.market_square()

    def interact_with_potion_mixer(self):
        if not self.__potion_mixer_interacted:
            print(self.potion_mixer.interact())

            while not self.__potion_mixer_interacted:
                interaction = int(input(f"1.) Ask about the ingredient\n"
                                        f"2.) Question {self.potion_mixer.name}\n"
                                        f"3.) Leave the potion mixer\n"))
                # Checks if the user has found the clue already
                # Else tell the user that you have the clue already
                if interaction == 1:
                    print(self.potion_mixer.say_dialogue("These ingredients I use here are not the herbs and "
                                                         "powders you find in this realm, these are blessed by the "
                                                         "lord that watches above us.\nIf I reveal too much it might "
                                                         "be the end of this town. \nSomethings are left untouched."))
                elif interaction == 2:
                    if self.potion_mixer.items not in self.user.inventory:
                        print(f"{self.user.name}: I have some questions for you to answer about the (cult's name)")
                        print(self.potion_mixer.perform_action("Looks at me terrifying as she screeches some "
                                                               "encrypted message as she runs away\n"))
                        print("Let's decipher what she said:\n")
                        cipher_decryption_game()
                        Level3.add_clue(self, "The Legendary Witch Slayer will save us all message")
                        print(f"You pick up some {self.potion_mixer.items} and decide to keep it.")
                        self.user.add_item(self.potion_mixer.items)
                        self.__potion_mixer_interacted = True
                    else:
                        print(f"{self.potion_mixer.name} is gone")
                elif interaction == 3:
                    print(self.potion_mixer.perform_action("Glares at you as you walk away from her"))
                    self.__potion_mixer_interacted = True
        else:
            print(f"You already interacted with {self.potion_mixer.name}")

        level3.market_square()

    def interact_with_street_performers(self):
        if not self.__street_performer_interacted:
            print(f"As {self.user.name} approaches the spectacular street performers, drawn by their routine.\n"
                  f"You began hearing the audience about a cloaked figure during the performance near the fountain of "
                  f"the market square.\nAnything you noticed?")
            print(self.street_performer.interact())
            Level3.add_clue(self, "Cloaked figure near fountain")
            print(f"As {self.user.name} thanked them, they couldn't stop wondering if this coincidental sighting"
                  "was a deliberate distraction.")
            self.__street_performer_interacted = True
        else:
            print(f"You already interacted with {self.street_performer.name}")

        level3.market_square()

    def tavern(self):
        print(f"You decide to head to the {self.current_location} "
              f"hoping to find the clues to continue your quest.\n"
              f"As you open the tavern door you see that's it filled with life as the melody playing"
              f"\nLaughter echoed off the wooden wall with such a song of a drinking making the patrons "
              f"stomping their feet in unison")

        while self.current_location == "Crown and Chalice Inn":
            action = input("\nWhat will you do?,\n"
                           "1) Interact with the drunken elves\n"
                           "2) Head to the bar\n"
                           "3) Leave the tavern\n")

            if action == "1":
                Level3.interact_with_elves(self)

    def interact_with_elves(self):
        for elf in self.drunken_elves:
            print(elf.interact())
            print(elf.perform_action(elf.actions))


if __name__ == "__main__":
    level3 = Level3(1, 100)
    level3.market()
