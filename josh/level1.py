"""
Author : Joshua Sunil Mathew
Program Description: OOP - Python Game Assignment ("Game Title")
Level 1



"""
import time
from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player  # Check if the import path is correct
from josh.challenges  import LibraryGame
from josh.knightfight import knightfight


class Level1(Location):
    def __init__(self, player, score):
        super().__init__("Citadel", ['Hall of Warriors', 'Grand Library', 'Armory', 'Druids Quarter'], ["Sir Smith", "Scribe"], [])
        self.current_location = self.sublocation[0]
        self.player = player
        self.score = score
        self.knight = NPC("Sir Smith", "It was a horrible sight, I remember each and every one of them", "We fought near the City Gates", "")
        self.scribe = NPC("Cedric the Scribe", "I've been doing some spring cleaning, sir!", "I don't know much! - but there have been scriptures of a hooded figure!", "Forbidden Manuscript")
        self.druid = NPC("David the Druid", f"Ive been expecting you {player.name}, We have a bit of a situation",
                          "",
                          "Chaos Sword")
        self.library1 = LibraryGame()

        self.interacted_scribe = False
        self.interacted_knight = False
        self.challengeAccepted = False
        self.levelCompleted = False
    def GameIntro(self):
        print("===================================")
        print("       Game          ")
        print("        Name! "
              "by Error 451           ")
        print("===================================")
        time.sleep(1)
        print("\nYou are about to embark on a quest veiled in the shadows.")
        time.sleep(1)
        print("Each level flows through the storyline, and you will be "
              "faced with puzzles"
              "\nand challenges!")
        time.sleep(1)
        print("Ready your weapons, gather your resolve and step into the unknown!")
        time.sleep(1)
        print("===================================")
    def HallOfWarriors(self):
        self.current_location = self.sublocation[0]
        print(f"Location: {self.current_location} - AD 734")
        time.sleep(1)
        print(
            "\nAs you walk down the dimly lit hallway of the citadel, the flickering torchlights cast an eerie glow on the frames that line the walls")
        time.sleep(1)
        print(
            "The Fallen Men - each portrait captures a haunting image, frozen in time. You feel the weight of the unknown pressing on you, and questions flood through your mind.")
        time.sleep(1)
        print("As you stare, The King's Knight approaches...")
        while True:
            player_choice = input(
                "Would you like to speak to the knight? 'y for yes' or 'n' for no : ")

            if player_choice.lower() == 'y' or 'yes':
                print(self.knight.interact())
                time.sleep(1)
                print(f"{player1.name}: Do you know where it happened")
                time.sleep(1)
                print(f"{self.knight.name}: {self.knight.clue()}")
                time.sleep(1)
                self.add_clue(self.knight.clue())
                self.interacted_knight = True
                self.player.coins = self.player.coins + 2
                print(f"You have: {self.player.coins} coins collected")
                break
            elif player_choice.lower() == 'n' or 'no':
                print("You must speak to the knight; he may have some insights...")

            else:
                print("Invalid Option, Try Again!")

        print("You walk towards the Druid's Quarters")
        time.sleep(3)
        self.DruidQuarter()
    def GrandLibrary(self):
        self.current_location = self.sublocation[1]
        print(f"Location : {self.current_location}")
        print("===================================\n")
        time.sleep(1)
        print(self.scribe.interact())
        time.sleep(1)
        print(self.druid.say_dialogue("Great Work, - I need the scriptures for the next sermon!"))
        time.sleep(1)
        print(self.scribe.say_dialogue("What brings you to the library?"))
        time.sleep(1)
        print(self.druid.say_dialogue("A light reading, does no harm"))
        time.sleep(1)
        print(self.druid.say_dialogue(f"Now {self.player.name}, Now onto Challenge 2! of your initiation"))
        self.library1.book_roulette()
        self.player.coins = self.player.coins + 3
        time.sleep(1)
        print(f"You have: {self.player.coins} coins collected")
        print(self.scribe.say_dialogue("Wow, that was impressive, - I may have some information for you to help you on journey"))
        print(f"{self.scribe.name}: {self.scribe.clue()}")
        self.add_clue(self.scribe.clue())
        self.interacted_scribe = True
        time.sleep(1)
        print(f"{self.druid}: I hear the Knight Would like to speak with you...")
        print(f"{self.druid}: Head to the Armory, for your Final Task!")
        self.Armory()


    def Armory(self):
        self.current_location = self.sublocation[2]
        print(f"\nLocation: {self.current_location}")
        print("===================================\n")
        time.sleep(1)
        print(self.knight.say_dialogue("Welcome to the Armory!"))
        print(self.knight.say_dialogue("Your Final Task, to Prove yourself worthy is to face me!"))
        print(self.knight.say_dialogue("I challenge you to a duel!"))
        knightfight()
        self.interacted_knight = True

    def DruidQuarter(self):
            self.current_location = self.sublocation[3]
            print(f"\nLocation: {self.current_location}")
            print("===================================\n")
            time.sleep(1)
            print(self.druid.interact())
            time.sleep(1)
            print(f"{self.player.name}: I have heard the stories, truly saddening! - why was I summoned here today?")
            print(self.druid.say_dialogue("We need an answer to all of this, why us of all people - THAT is why YOU are here!"))
            while True:
                print(self.druid.say_dialogue("I have a quest for you, whether you choose to accept it"))
                time.sleep(1)
                player_choice = input("Would you like to accept the quest? -> 'y for yes' or 'n' for no : ")
                if player_choice.lower() == 'y':
                    print(self.druid.say_dialogue("\nI knew this day would come!, but before you begin you must prove to me that you are capable to embark on this quest!"))
                    time.sleep(1)
                    print(self.druid.say_dialogue("It will test your mental, physical and quick thinking abilities!"))
                    time.sleep(1)
                    print(self.druid.say_dialogue("Let us Begin! - with a quick riddle!"))
                    time.sleep(1)
                    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"

                    print(f"Riddle: {riddle}")
                    print("1. Sound, 2. Echo, 3. Light")
                    time.sleep(1)
                        # Get the player's answer
                    player_answer = (input("Your answer: "))

                    # Check if the player's answer is correct
                    if player_answer.lower() == "echo" or '2':
                        print("Congratulations! You've solved the riddle! - here is 3 coins")
                        time.sleep(1)
                        self.player.coins = self.player.coins + 3
                        time.sleep(1)
                        print(f"YOUR CURRENT COINS: {self.player.coins}")
                        time.sleep(1)

                        print(f"{self.druid.name}: Great work, {self.player.name}! - Lets head to the library for your next challenge")
                        time.sleep(1)
                        self.GrandLibrary()
                        break
                    else:
                        print(f"{self.druid.name: looks doubtful...}")
                        print("Unfortunately, that's not the correct answer. Keep trying!")

                else:
                    print(self.druid.say_dialogue("Maybe I had made a mistake in summoning you..."))
                    print("\nYou must complete the Druid's Activities to continue further in this level!")








if __name__ == "__main__":
    player = input("Enter a player name to immerse yourself in the story: ")
    player1 = Player(f"{player}")
    time.sleep(1)
    player1.coins = 0
    level1 = Level1(player1, 0)  # Pass the player object to Level1 constructor
    level1.GameIntro()
    level1.HallOfWarriors()  # Call the method on the instance
