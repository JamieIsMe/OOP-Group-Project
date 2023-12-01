"""
Author : Joshua Sunil Mathew
Program Description: OOP - Python Game Assignment ("Game Title")
Game Intro
Level 1
The Citadel : The player admires the portraits on the wall and is approached by the
knight(NPC)
- Then leads to the druid's quarters where the option is given to accept the quest
- The Druid has 3 challenges for the player in 3 rooms within the Citadel,
Druid's Quarters, The Great Library, The Armory
Each challenge has an assortment of puzzles for the player to complete,
leading to the reward of coins / clues
However the Final Level - is a duel with knight, to earn the {item}
The with all the clues, coins received -
the player heads to the City Walls - Seán's Level 2

Developed by Error 451

"""
# GAME IMPORTS
import time
from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player
from josh.challenges import DruidGame, Challenges
from josh.FinalDuel import Duel



# LEVEL 1 CLASS
class Level1(Location):
    def __init__(self, player):
        super().__init__("Citadel",
                         ['Hall of Warriors','Grand Library', 'Armory',
                          'Druids Quarter'],
                         ["Sir Smith", "Scribe"], [])

        self.current_location = self.sublocation[0]
        self.player = player

        self.knight = NPC("Sir Smith",
                          "It was a horrible sight,"
                          " I remember each and every one of them","near the City "
                                                                   "Gates","",
                          "")

        self.scribe = NPC("Cedric the Scribe",
                          "I've been doing some spring cleaning, sir!","hooded figures dwelling near the City",
                          "Forbidden Manuscript",
                          "")

        self.druid = NPC("David the Druid",
                         f"Ive been expecting you {player.name},"
                         f" We have a bit of a situation",
                         "",
                         "Chaos Sword","")

        self.library1 = Challenges()
        self.druidgame = DruidGame()
        self.finalduel = Duel()
        self.__game_started = False
        self.interacted_scribe = False
        self.interacted_knight = False
        self.interacted_druid = False
        self.challengeAccepted = False
        self.level_running = True

    def level_start(self):
        self.GameIntro()

    def update(self):
        if not self.__game_started:
            player_input = input("Press 'q' to quit or 's' to start: ")
            if player_input.lower() == "q":
                print("Till another time, adventurer!")
                self.__running = False
            elif player_input.lower() == "s":
                print("Ready your weapons, gather your resolve and "
                      "step into the unknown!")
                self.__game_started = True
                time.sleep(2)
                self.HallOfWarriors()
            else:
                print("Invalid Input!")
                self.update()


    # BEGIN GAME INTRO TITLES
    def GameIntro(self):
        print("===================================")
        print("       The Vanishing Veil        ")
        print("         Cult of Shadows          ")
        print(" an adventure, developed by Error 451")
        print("===================================")

        time.sleep(1)

        print("\nYou are about to embark on a quest veiled in the shadows.")
        time.sleep(1)
        print("Each level flows through the storyline, and you will be "
              "faced with puzzles"
              "\nand challenges!")

        time.sleep(1)
        self.update()

        time.sleep(1)

        print("===================================")

        #END OF GAME INTRO

    def summary(self):
        print("\n==================== Level 1 Player Summary ====================")
        print(f"Player Name: {self.player.name}")
        print(f"Player Coins: {self.player.coins} coins")
        #print(f"Player Inventory: {self.player.inventory}")
        #print(f"Clues: {self.player.show_clues()}")


        # ADD LEVELS PROGRESSED (logging)
        print("==================== End of Player Summary ====================\n")

    def HallOfWarriors(self):
        self.current_location = self.sublocation[0]
        print("==================================")
        print(f"(Location: {self.current_location} - AD 734)")
        print("==================================")
        time.sleep(2)
        print("\nAs you walk down the dimly lit hallway of the citadel, "
        "the flickering torchlights cast an eerie glow on the frames that"
        "line the walls")

        time.sleep(1)
        print(
            "The Fallen Men - each portrait captures a haunting image,"
            " frozen in time. You feel the weight of the unknown pressing on you"
            ", and \nquestions flood through your mind.")

        time.sleep(1)
        print("As you stare, The King's Knight approaches...")
        while True:
            player_choice = input("\n(Would you like to speak to the knight?) 'y for yes' or 'n' for no : ")

            if player_choice.lower() == 'y' or player_choice.lower() == 'yes':
                time.sleep(1)
                print(f"\n{self.knight.interact()}")
                time.sleep(2)
                print(f"{self.player.name}: Do you know of where it happened?")
                time.sleep(2)
                print(
                    self.knight.say_dialogue(
                        "The battle was near the the city gates!"))
                time.sleep(3)
                self.add_clue(self.knight.clue())
                self.interacted_knight = True
                time.sleep(1)
                print("(You earned 2 coins for interacting with the knight!)")
                self.player.coins += 2
                time.sleep(1)
                print(f"(You have: {self.player.coins} coins collected)\n")
                time.sleep(1)
                break

            elif player_choice.lower() == 'n' or player_choice.lower() == 'no':
                print("(You must speak to the knight; he may have some insights...)")

            else:
                print("(Invalid Option, Try Again!)")

        print("You walk towards the Druid's Quarters")
        print("Walking...")
        time.sleep(3)
        self.DruidQuarter()

    def GrandLibrary(self):
        self.current_location = self.sublocation[1]
        print("==================================")
        print(f"Location : {self.current_location}")
        print("===================================\n")
        print("(You approach Cedric, The Library Scribe)\n")
        time.sleep(2)
        print(self.scribe.interact())
        time.sleep(1)
        print(self.druid.say_dialogue(
            "Great Work, - I need those scriptures for the next sermon!"))
        time.sleep(1)
        print(self.scribe.say_dialogue(f"They are ready to go sir!,"
                                       f" Anyways! What brings you and {self.player.name} to the library?"))
        time.sleep(1)
        print(self.druid.say_dialogue("A light reading per say, doth no harm!\n"))
        time.sleep(1)
        print(self.druid.say_dialogue(
            f"now {self.player.name}, onto Challenge 2 of your test!\n"))
        self.library1.book_roulette()
        self.player.coins = self.player.coins + 3
        time.sleep(1)
        print(f"You have: {self.player.coins} coins collected\n")
        print(self.scribe.say_dialogue("Wow, that was impressive, - I may have some information for you to help you on journey\n"))
        print(self.scribe.say_dialogue("I don't know much, but I did read of some hooded people dwelling, in the City"))
        self.add_clue(self.scribe.clue())
        print("\n")
        self.interacted_scribe = True
        time.sleep(1)
        print(self.druid.say_dialogue("I hear the King's Knight has heard you success and would like to speak with you..."))
        time.sleep(1)
        print(self.druid.say_dialogue("proceed to the Armory, for your final Challenge!"))
        print("Heading to the Armory...")
        time.sleep(5)
        self.Armory()

    def Armory(self):
        self.current_location = self.sublocation[2]
        print("==================================")
        print(f"\n(Location: {self.current_location})")
        print("===================================\n")
        time.sleep(1)
        print(self.knight.say_dialogue("Welcome to the Armory!"))
        print(self.knight.say_dialogue("Your Final Task, to Prove yourself worthy is to face me!"))
        print(self.knight.say_dialogue("Lets see, how good you really are!"))
        print(self.knight.say_dialogue("\nI challenge you to a duel!"))
        print(self.knight.say_dialogue("Winner gets the greatest weapon, passed down from generation to generation: 'The Chaos Sword!"))
        self.level_running = self.finalduel.duel()
        if not self.level_running:

            self.interacted_knight = True
            time.sleep(1)
            self.player.coins = self.player.coins + 10
            print("You have been awarded 10 coins!")
            time.sleep(1)
            print(f"You have: {self.player.coins} coins collected")

            print(self.knight.say_dialogue("You have certainly, exceeded my expectations!"))
            print(self.knight.say_dialogue("You have a long adventure ahead of you, my friend!"))
            self.player.add_item('Chaos Sword')
            print("Chaos Sword Added to Inventory!")
            self.player.show_inventory()

            print(self.druid.say_dialogue( "You have certainly, exceeded my expectations!"))

            print(self.druid.say_dialogue(f"Best of Luck, {self.player.name}"))
            print(self.druid.say_dialogue(f"Best of Luck, {self.player.name}"))

            print(f"{self.player.name}: Lets head to the city!\n")

            self.summary()
        else:
            pass
            # if you have not defeated the knight


    def DruidQuarter(self):
        self.current_location = self.sublocation[3]

        time.sleep(3)
        print("==================================")
        print(f"(Location: {self.current_location})")
        print("==================================\n")
        time.sleep(1)
        print(self.druid.interact())

        time.sleep(1)
        print(f"{self.player.name}: I have heard the stories, truly saddening! - why was I summoned here today?")
        time.sleep(1)
        print(self.druid.say_dialogue("We need an answer to all of this, why us of all people - THAT is why YOU are here!\n"))
        time.sleep(1)

        print(self.druid.say_dialogue("I have a quest for you, whether you choose to accept it"))
        time.sleep(1)

        while True:
            player_choice = input("Would you like to accept the quest? -> 'y' for yes or 'n' for no: ")

            if player_choice.lower() == 'y':
                time.sleep(1)
                print(self.druid.say_dialogue(
                    "The <cultname> have been the main link to our missing people,\nThey are a group of hooded people, hiding within our society"
                    "\nWe have held our silence for too long and longed for someone to step up!\n"))
                time.sleep(4)
                print(self.druid.say_dialogue(
                    "But before you begin you must prove to me that you are capable to embark on this quest\n"))
                time.sleep(1)
                print(self.druid.say_dialogue(
                    "It will test your mental, physical "
                    "and quick thinking abilities\n"))
                time.sleep(2)
                self.druidgame.catch_ball()

                time.sleep(1)
                self.player.coins = self.player.coins + 3
                print("You have been awarded 3 coins!")
                time.sleep(1)
                print(f"You have: {self.player.coins} coins collected")
                time.sleep(1)
                print(f"{self.druid.name}: Great Catches, {self.player.name}! - Let us head to the Grand Library, for your next challenge")
                print("Walking...\n")
                time.sleep(4)
                break

            else:
                print(self.druid.say_dialogue("Maybe I had made a mistake in summoning you..."))
                print("\n(You must complete the Druid's Activities to continue further in this level!)")

        self.GrandLibrary()


if __name__ == "__main__":
    # PLAYER NAME SELECTION
    player = input("\nEnter a player name to immerse yourself in the story: ")
    player1 = Player(f"{player}")
    time.sleep(1)  # DELAY
    # MAKE PLAYER COINS 0
    player1.coins = 0
    # PASS PLAYER TO LEVEL 1
    level1 = Level1(player1, 0)
    # INSTANCE OF GAME INTRO - GAME TITLE & INTRO
    level1.GameIntro()
    # BEGIN SUB LOCATION 1

