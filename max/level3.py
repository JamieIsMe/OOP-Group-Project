"""
Program Name: level3.py

Author: Max Ceban

Program Description:

This is the third level out of our six-level game.
This level will mess with the player/Red Herring.
This is set in the middle of the town in which the player will need to solve riddles by npcs.
The clues collected throughout the level will lead to a plot twist in our player's quest.
The player can react with the merchants and can buy items that can enhance gameplay.

Date: 25/11/2023
"""
# Import the necessary dependencies, Location, Player, and NPC classes
from denis.Player import Player
from sean.locationClass import Location
from sean.fight import fight, User, CultMember
from cian.characters import NPC
from max.minigame import cipher_decryption_game
from max.riddle import riddle_game


class Level3(Location):
    """
        This class represents the third level of the game and inherits from the Location class.
        It includes specific locations and NPCs for the level.
    """

    def __init__(self, player):
        super().__init__("Town Center", ["Market", "Crown and Chalice Inn", "Haven's Port"],
                         ["Textile Merchant", "BlackSmith", "Potion Mixer", "Street Performers",
                          "Tavern keeper"], [])

        self.player = player
        self.current_location = self.sublocation[0]
        self.side_quest_enabled = False

        self.blacksmith = NPC("Astrid Steelheart",
                              ["Welcome to the Iron-heart Forge. What brings you here today adventurer? "
                               "\nNew armor, maybe new tools or a legendary sword for you?"],
                              "Seen some cloaked folks gone to the potion mixer for some potions.", "Sword",
                              "")

        self.textile_merchant = NPC("Elara Looming",
                                    ["Dear patrons, welcome to the world of wonder!\n"
                                     "Step into the world of Velvet Haven Textiles, where every thread tells a story "
                                     "and every fabric whispers its unique story."], "Paper with the cult logo",
                                    "Fur coat", "")

        self.potion_mixer = NPC("Gwyneth Gerald",
                                ["Ah, hello, adventurer! Enter the mystical embrace of Gwyneth's sorcery.\n"
                                 "There, the air is filled with the enchanting essence of unknown possibilities."],
                                "Deciphered Message", "Spellbook", "")

        self.street_performer = NPC("The juggler",
                                    ["Yeah, saw someone briefly, but they vanished into the crowd. Might "
                                     "be nothing"], "Cloaked figure near fountain", " ", "")

        self.drunken_elf1 = NPC("Aricen Emberheart",
                                ["You know what's the best part about being an elf? We're like, "
                                 "timeless, man. I've got all the time in the world to enjoy "
                                 "this tavern!"], "", "",
                                ["swaying on the stool"])

        self.drunken_elf2 = NPC("Clarista Starfall", ["Timeless? I think you've had too much elven wine, friend. "
                                                      "You've got tomorrow morning catching up with you."],
                                "", "", ["raising an eyebrow"])

        self.drunken_elf3 = NPC("Thandor Dawnwhisper",
                                ["Present, future, who cares? I'm just here for the company and the questionable "
                                 "decisions!"], "", "", ["joining the conversation"])

        self.drunken_elves = [self.drunken_elf1, self.drunken_elf2, self.drunken_elf3]

        self.tavern_keeper = NPC("Finnegan McCathy", ["Ceád míle fáilte to all ye weary wanderer!."],
                                 "Cult heading to the port", "", "Leaned me on me glaring to my soul")

        self.cult_member = NPC("Cult Member", " ", "", "Map leading the player", "")

        self.craftsman = NPC("Malik Thompson",
                             ["Greetings, friend! What brings you to my humble abode?",
                              "Are you in need of a piece that tells a story or seeking the magic that can be found "
                              "in the heart of crafted wonders?"], "", "Feathernutter",
                             ["Protecting Feathernutter", "Humming a rhythm", "Playing an instrument"])

        # Boolean Variables set for no double interaction between any npcs
        self.__blacksmith_interacted = False
        self.__textile_merchant_interacted = False
        self.__potion_mixer_interacted = False
        self.__street_performer_interacted = False
        self.__drunken_elves_interacted = False
        self.__tavern_keeper_interacted = False
        self.__craftsman_interacted = False

    def level_start(self):
        print(f"You steps afoot to the town center of (Town name) lively {self.current_location}"
              f" square after (Ending of level 2),\n"
              f"where colourful stalls filled with treasure, the savory wonderful scent of roasting meats, "
              f"\nwith mesmerising street performances happening at the minute with camaraderie underneath the cold "
              f"snowy night.")
        self.market()

    def market(self):
        while self.current_location == "Market":
            action = input("\nWhat will you do?,\n"
                           "1) Take a look around the market\n"
                           "2) Go to the tavern\n"
                           "3) Go to the Port\n")
            if action == "1":
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
            elif action == "2":
                self.current_location = self.sublocation[1]
                Level3.tavern(self)
            elif action == "3":
                self.current_location = self.sublocation[2]
                Level3.port(self)

    def market_square(self):
        while True:
            try:
                character = int(input("\nWho do you want to interact with:\n"
                                      "1) Blacksmith\n"
                                      "2) Textile Merchant\n"
                                      "3) Potion Mixer\n"
                                      "4) See the street performers\n"
                                      "5) Leave the market square.\n"))
                match character:
                    case 1:
                        print("\n")
                        if not self.__blacksmith_interacted:
                            Level3.interact_with_blacksmith(self)
                        else:
                            print(f"You already interacted with {self.blacksmith.name}")
                    case 2:
                        print("\n")
                        if not self.__textile_merchant_interacted:
                            Level3.interact_with_textile_merchant(self)
                        else:
                            print(f"You already interacted with {self.textile_merchant.name}")
                    case 3:
                        print("\n")
                        if not self.__potion_mixer_interacted:
                            Level3.interact_with_potion_mixer(self)
                        else:
                            print(f"You already interacted with {self.potion_mixer.name}")
                    case 4:
                        print("\n")
                        if not self.__street_performer_interacted:
                            Level3.interact_with_street_performers(self)
                        else:
                            print(f"You already interacted with {self.street_performer.name}")
                    case 5:
                        Level3.market(self)
                        break
                    case _:
                        print("Invalid choice")
            except ValueError as ve:
                print(f"{ve} invalid input it must be a number")

    def interact_with_blacksmith(self):
        print(self.blacksmith.say_dialogue(self.blacksmith.dialogue[0]))  # BLACKSMITH SPEAKS VOICE-LINE

        while not self.__blacksmith_interacted:
            interaction = int(input(f"1.) Question {self.blacksmith.name} about the cult\n"
                                    f"2.) Ask about forging a sword\n"
                                    f"3.) Leave the blacksmith\n"))
            # Checks if the user has found the clue already
            # Else tell the user that you have the clue already
            if interaction == 1:
                print(f"{self.player.name}: Have you heard about the (Cult name) around abducting people "
                      "recently.")
                print(self.blacksmith.say_dialogue("Yeah the market have been talking about the news."))
                print(self.blacksmith.say_dialogue("One of the merchants reported that they have went to "
                                                   f"the potion mixer as of recently."))
                Level3.add_clue(self, "Blacksmith's observation on the potion mixer")
            elif interaction == 2:
                if self.blacksmith.items not in self.player.inventory:
                    print(self.blacksmith.say_dialogue("Ohh you interested in crafting an fine piece metal then"
                                                       "you have to pay for it, it'll be 100 coins please."))
                    # An extra option depending on the score of the player
                    action = input(f"Want to purchase a sword for 100 coins?\n"
                                   "Yes: Y\n"
                                   "No: N\n")
                    if action.lower() == "y":
                        if self.player.coins >= 100:
                            print(self.blacksmith.say_dialogue("Here's your new sword wanderer, you must name "
                                                               f"your sword for your future battle."))
                            self.player.coins = self.player.coins - 100
                            print(f"New balance: {self.player.coins}")
                            print(self.blacksmith.say_dialogue(f"The sword suits you traveler, this "
                                                               f"will help you for sure"))
                            self.player.add_item(self.blacksmith.items)
                        else:
                            print(self.blacksmith.say_dialogue("You don't have enough coins for the sword."))
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
                print("Invalid option")

    def interact_with_textile_merchant(self):
        if "Fluffernutter the Chicken" not in self.player.inventory and not self.side_quest_enabled:
            print(self.textile_merchant.say_dialogue(self.textile_merchant.dialogue[0]))

            while not self.__textile_merchant_interacted:
                interaction = int(input(f"1.) Ask about the newest trends in the shop\n"
                                        f"2.) Question {self.textile_merchant.name}\n"
                                        f"3.) Leave the textile merchant\n"))
                # Checks if the user has found the clue already
                # Else tell the user that you have the clue already
                if interaction == 1:
                    if self.textile_merchant.items not in self.player.inventory:
                        print(self.textile_merchant.say_dialogue(
                            "Discover our collection of popular trends in intricate embroidery, sumptuous velvet, "
                            "and natural, earthy tones.\nYou can also expect shimmering metallic threads, breathable "
                            "linens, and gorgeous brocade fabrics, each fabric unique in its own way.\nIt tells a story"
                            " of elegance."))

                        action = input("You take a gander around the shop and seek upon a fur coat for 100 coins.\n"
                                       "Do you wish to purchase it?\n"
                                       "Yes: Y\n"
                                       "No : N\n")

                        if action.lower() == "y":
                            if self.player.coins >= 100:
                                print(
                                    self.textile_merchant.say_dialogue(f"I see the fur coat interests you, this is "
                                                                       f"yours now wanderer it might help in the "
                                                                       f"extreme weather conditions ahead of your "
                                                                       f"journey."))
                                self.player.add_item(self.textile_merchant.items)
                            else:
                                print(
                                    self.textile_merchant.say_dialogue("You do not have another coins for the fur "
                                                                       "coat,\nadventurer perhaps maybe you can find "
                                                                       "my missing cherished chicken Fluffernutter, "
                                                                       "and my heart aches without its presence.\n"
                                                                       "I may provide a extra reward onto of this as "
                                                                       "well."))  # SIDE QUEST FOR THE LEVEL

                                action = input("Do want to take part in the side quest?\n"
                                               "Yes: Y\n"
                                               "No: N\n")

                                if action.lower() == "y" or action.capitalize() == "Y":
                                    print(self.textile_merchant.say_dialogue(
                                        "Oh, thank the stars! You're a true lifesaver "
                                        "for agreeing to help me with my little "
                                        "feathered friend.\n"
                                        "My prized chicken, Fluffernutter, has gone "
                                        "missing, and I've been in a complete tizzy."))
                                    print(f"{self.player.name}: No worries! I'm happy to help."
                                          f"\nWhere should I start looking?")
                                    print(self.textile_merchant.say_dialogue("Thank you for taking on the "
                                                                             "quest!\nFluffernutter was last seen at "
                                                                             "the port.\nPlease take this feed to "
                                                                             "lure them back.\nI'll reward you "
                                                                             "generously once you bring my chicken "
                                                                             "home safely. Good luck, and may your "
                                                                             "journey be swift!"))
                                    print(
                                        f"{self.player.name}: I'll find Fluffernutter and bring them back, don't worry!")
                                    print("We leave the shop knowing we have a side quest to do!")
                                    self.side_quest_enabled = True
                                    self.__textile_merchant_interacted = True
                                    self.__craftsman_interacted = False
                                    Level3.market(self)
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
                    print(self.textile_merchant.perform_action(
                        "Waves nervously as I leave the stores maybe its just \n"
                        "something in his mind"))
                    self.__textile_merchant_interacted = True
        else:
            print(self.textile_merchant.say_dialogue("Thanks a bunch for rescuing my wayward chicken. "
                                                     "To show my appreciation, here's a sturdy armor for you – "
                                                     "and a pouch with 75 coins.\n"
                                                     "Never expected a chicken chase to turn into such an adventure!\n"
                                                     "If you ever need more help or encounter more feathered mischief, "
                                                     "you know where to find me.\nSafe travels!"))
            self.player.remove_item("Fluffernutter the Chicken")
            self.player.add_item("Armor")
            self.player.name = self.player.name + 75
            self.side_quest_enabled = False
            level3.market_square()

    def interact_with_potion_mixer(self):
        print(self.potion_mixer.say_dialogue(self.potion_mixer.dialogue[0]))

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
                if self.potion_mixer.items not in self.player.inventory:
                    print(f"{self.player.name}: I have some questions for you to answer about the (cult's name)")
                    print(self.potion_mixer.perform_action("Looks at me terrifying as she screeches some "
                                                           "encrypted message as she runs away\n"))
                    print("Let's decipher what she said:\n")
                    cipher_decryption_game()
                    Level3.add_clue(self, "The Legendary Witch Slayer will save us all message")
                    print(f"You pick up some {self.potion_mixer.items} and decide to keep it.")
                    self.player.add_item(self.potion_mixer.items)
                    self.__potion_mixer_interacted = True
                else:
                    print(f"{self.potion_mixer.name} is gone")
            elif interaction == 3:
                print(self.potion_mixer.perform_action("Glares at you as you walk away from her"))
                self.__potion_mixer_interacted = True

        level3.market_square()

    def interact_with_street_performers(self):
        print(f"As {self.player.name} approaches the spectacular street performers, drawn by their routine.\n"
              f"You began hearing the audience about a cloaked figure during the performance near the fountain of "
              f"the market square.\nAnything you noticed?")
        print(self.street_performer.interact())
        Level3.add_clue(self, "Cloaked figure near fountain")
        print(f"As {self.player.name} thanked them, they couldn't stop wondering if this coincidental sighting"
              " was a deliberate distraction.")
        self.__street_performer_interacted = True

        level3.market_square()

    def tavern(self):
        print(f"You decide to head to the {self.current_location} "
              f"hoping to find the clues to continue your quest.\n"
              f"As you open the tavern door you see that's it filled with life as the melody playing"
              f"\nLaughter echoed off the wooden wall with such a song of a drinking making the patrons "
              f"stomping their feet in unison")

        while self.current_location == "Crown and Chalice Inn":
            try:
                action = int(input("\nWhat will you do?,\n"
                                   "1) Interact with the drunken elves\n"
                                   "2) Head to the bar\n"
                                   "3) Leave the tavern\n"))
                match action:
                    case 1:
                        if not self.__drunken_elves_interacted:
                            Level3.interact_with_elves(self)
                        else:
                            print("You interacted with the elves already")
                    case 2:
                        if not self.__tavern_keeper_interacted:
                            Level3.bar(self)
                        else:
                            print("You interacted with the tavern keeper already")
                    case 3:
                        self.current_location = self.sublocation[0]
                        Level3.market(self)
                    case _:
                        print("Invalid option")
            except ValueError as ve:
                print(f"{ve} input should be a number")

    def interact_with_elves(self):
        for elf in self.drunken_elves:
            print(elf.say_dialogue(elf.dialogue))
            print(elf.perform_action(elf.actions))

        while self.current_location == self.sublocation[1]:
            interaction = int(input(f"1.) Ask about the tavern's history\n"
                                    f"2.) Question the elves\n"
                                    f"3.) Leave the elves alone\n"))
            if interaction == 1:
                print(
                    self.drunken_elf1.say_dialogue("Established in 1685, The Crown and Chalice Inn in Eldenhaven is a "
                                                   "historic hub, \n once a haven for travelers and now a charming "
                                                   "space for"
                                                   "locals and visitors. The inn's name, 'The Crown and Chalice,"
                                                   "' \n nods to the town's noble heritage. With its exposed beams and "
                                                   "faded"
                                                   "tapestries, the inn invites patrons to step into Eldenhaven's rich "
                                                   "history"))
                print(self.drunken_elf2.say_dialogue("Hey adventurer Why did the ghost refuse to haunt The Crown and "
                                                     "Chalice Inn?"))

                print(self.drunken_elf3.say_dialogue("Because the spirits were too high, and he couldn't find a "
                                                     "'boo'-th to himself"))

                print("(They clink mugs and burst into laughter, to the bemusement of other tavern patrons.)")
            elif interaction == 2:
                if "Elves' observation on the tavern keeper" not in self.clues:
                    print(self.drunken_elf2.say_dialogue("Hark, ye noble celebrant! Prepare thy wit for a riddle from "
                                                         "days of yore!\nWhat be the thing with a golden head, "
                                                         "silver tail, and no body, yet it dances through the air "
                                                         "with a"
                                                         "fiery trail? \nEngage thy mind in this medieval mystery and "
                                                         "let"
                                                         "the revelry continue! "))

                    print(self.drunken_elf2.perform_action("leaning against my face."))

                    action = input("Want to try and solve it? 'y' or 'n':\n")

                    if action.lower() == "y" or action.capitalize() == "Y":
                        riddle_game()
                        print(self.drunken_elf1.say_dialogue("🕯️ Congrats, Riddle Master! You've cracked the "
                                                             "medieval mysteries like a goofy genius!\n🎉 May your "
                                                             "candles always burn bright,\nhorses gallop swift, "
                                                             "and dragons... well,\nstay mythical and mysterious! "
                                                             "Keep rocking those riddles with a touch of "
                                                             "goofiness!\n🤩👑"
                                                             "#RiddleChampion 🕵️‍♂️🏰 "))
                        print(self.drunken_elf2.say_dialogue("We heard a cult member's discuss with the tavern "
                                                             "keeper"
                                                             "on booking the venue soon speak with the keeper"))
                        Level3.add_clue(self, "Elves' observation on the tavern keeper")
                    elif action.lower() == "n" or action.capitalize() == "N":
                        pass
                else:
                    print("You solved the riddle already!")
            elif interaction == 3:
                self.__drunken_elves_interacted = True
                break
            else:
                print("Invalid option")

    def bar(self):
        if "Elves' observation on the tavern keeper" not in self.clues:
            print(f"{self.player.name}: I feel like there's something I need to know before I do this")
        else:
            print("You have the observation from the elves in which you go to the Tavern Keeper")
            print(self.tavern_keeper.say_dialogue(self.tavern_keeper.dialogue[0]), "\u2618\ufe0f")
            print(
                f"{self.player.name}: I've been hearing around from the locals that the (CULT NAME) is terrorizing this "
                f"Eldenhaven \nabducting people and committing satanic rituals to them,\nyou seem to know something "
                f"\U0001F914")
            print(self.tavern_keeper.say_dialogue("Aye, I've heard of the (CULT NAME) terrorizing Eldenhaven.\n"
                                                  "Whispers speak of abductions and dark rituals.\nTread carefully, "
                                                  "friend.\nThe cult operates in shadows at the port, "
                                                  "and prying eyes may attract their malevolent gaze."))
            Level3.add_clue(self, "Cult at the port")
            self.__tavern_keeper_interacted = True

    def port(self):
        print("Welcome to Haven's Harbour, a medieval harbour full of marine legends and lively commerce.\n"
              "Sturdy ships with aged sails dock next to cobblestone alleys where merchants peddle strange "
              "items.\n")

        print("Locals who rely on the sea for their livelihood, bringing in fresh catches to supply the town and its "
              "taverns.\n")

        print("Defenders of the port, maintaining order and ensuring the safety of its inhabitants.\n")

        if "Cult at the port" not in self.clues:
            while self.current_location == self.sublocation[2]:
                try:
                    action = int(input("\nWhat will you do?,\n"
                                       "1) Interact with the Craftsman\n"
                                       "2) Leave Haven's Port\n"))
                    match action:
                        case 1:
                            if not self.__craftsman_interacted:
                                self.interact_with_craftsman()
                            else:
                                print("You interacted with the craftsman already")
                        case 2:
                            self.current_location = self.sublocation[0]
                            Level3.market(self)
                        case _:
                            print("Invalid option")
                except ValueError as ve:
                    print(f"{ve} input needs to be a integer")
        else:
            print(
                "Beneath the moonlit port, a clandestine cult engaged in an ominous ritual.\n"
                f"{self.player.name} confronted them, demanding answers.\n"
                "Interfering with our sacred gathering, detective? the cult leader hissed.\n"
                "Undeterred, the detective stood firm.\n"
                "Laughter echoed as the cult chanted, conjuring an eerie ambiance.\n"
                "Tension peaked, and a cult member lunged at the detective.\n"
                "A brief but intense struggle ensued. The detective, skilled and resourceful, "
                "managed to subdue the assailant.\n"
                "As backup sirens approached, the defeated cult member vanished into the shadows.\n"
                "The detective, now more determined, unravels the dark secrets concealed within the port,"
                " knowing that this encounter was just the beginning of a greater mystery.\n")

            user = User(self.user.name)
            cult_member = CultMember()
            final_fight = fight(user, cult_member)

            if final_fight:
                self.player.add_item(final_fight)
                self.player.show_inventory()
                Level3.ending()

    def interact_with_craftsman(self):
        if self.side_quest_enabled:
            print("As you approach Fluffernutter near the port, you notice a burly craftsman holding the chicken in "
                  "his hands, a mischievous glint in his eyes.")

            print("Well, well, what have we here? Seems like you're looking for this feathery friend. If you want "
                  "your precious chicken back, you'll have to pay a toll of 35 coins.\nFluffernutter's freedom comes "
                  "at a price, my friend")

            action = input("Fluffernutter squawks as if in agreement. What's your response?\n"
                           "Yes: Y\n"
                           "No: N\n")

            if action.lower() == "y" or action.capitalize() == "Y":
                if self.player.coins >= 35:
                    print(f"{self.player.name} reach into their pouch and count out the required 35 coins."
                          f"\nWith a reluctant sigh,they hand the coins over to the craftsman, who smirks triumphantly.")
                    print(self.craftsman.say_dialogue("Smart choice, my friend. Fluffernutter is free to go."))
                    print(self.craftsman.perform_action("the craftsman releases the chicken, who scurries back to the "
                                                        "player."))
                    self.player.add_item("Fluffernutter the Chicken")
                    self.player.name = self.player.name - 35
                    print("Coins: ", self.player.name)
                    self.__textile_merchant_interacted = False
                    print(f"I can bring him back now to {self.textile_merchant.name}")
                else:
                    print(self.craftsman.say_dialogue("Well, well. Seems like you're a bit short on funds. I can't "
                                                      "just release Fluffernutter for free, you know.\n You've got one "
                                                      "options: scrounge up the coins. Otherwise, your feathery "
                                                      "friend stays in my grasp."))
            elif action.lower() == "n" or action.capitalize() == "N":
                print(self.craftsman.say_dialogue("Stubborn, aren't you? Well, if you won't pay.\nFluffernutter stays "
                                                  "with me until you pay up."))
            else:
                print("Invalid Input")
        else:
            print(
                "As you approach the vibrant workshop, the rhythmic sound of metal hitting metal and the sweet scent of"
                " exotic woods will greet you.\n"
                "The artist, a sturdy figure with warm earth-toned skin and decorated with colorful fabrics, "
                "looks up from his work as you enter.")

            print(self.craftsman.say_dialogue(self.craftsman.dialogue[0]))
            print(self.craftsman.say_dialogue(self.craftsman.dialogue[1]))

            print("Their eyes are filled with wisdom and a deep understanding of the craft, reflecting the pride and "
                  "heritage attached to each piece.\nIt is clear that this artist's work not only reflects his know-how"
                  "but also carries with it the rich traditions and stories of his African roots.")

        self.__craftsman_interacted = True

    def ending(self):
        print(
            f"The subdued cult member carried a cryptic map, revealing a path through a mushroom forest and a goblin camp. "
            f"Undeterred, {self.player.name} follows the mystical trail, uncovering the cult's hidden home base. "
            "As they venture through enchanted landscapes, "
            "the air thickens with mystery, setting the stage for a perilous journey into the heart of darkness.")


if __name__ == "__main__":
    player = Player("")
    level3 = Level3(player)
    level3.market()
