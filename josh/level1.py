import time
from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player  # Check if the import path is correct


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

        self.interacted_scribe = False
        self.interacted_knight = False
        self.challengeAccepted = False
        self.levelCompleted = False
    def GameIntro(self):
        print("===================================")
        print("        Shadows of the            ")
        print("        Forgotten Realm             ")
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
                "\nWould you like to speak to him? 'y for yes' or 'n' for no : ")

            if player_choice.lower() == 'y':
                print(self.knight.interact())
                time.sleep(1)
                print(f"{player.name}: Do you know where it happened")
                time.sleep(1)
                print(f"{self.knight.name}: {self.knight.clue()}")
                time.sleep(1)
                self.add_clue(self.knight.clue())
                self.interacted_knight = True
                self.player.coins = self.player.coins + 2
                print(f"YOUR CURRENT COINS: {self.player.coins}")
                break
            elif player_choice.lower() == 'n':
                print("You must speak to the knight; he may have some insights...")

            else:
                print("Invalid Option")

        print("You walk towards the Druid's Quarters")
        time.sleep(2)
        self.DruidQuarter()
    def GrandLibrary(self):
        self.current_location = self.sublocation[1]
        print(f"{self.current_location}")
        time.sleep(1)
        print(self.scribe.interact())
        time.sleep(1)
        print(self.druid.say_dialogue("Great Work, - I need the scriptures for the next sermon!"))
        time.sleep(1)
        print(self.scribe.say_dialogue("What brings you to the library?"))
        time.sleep(1)
        print(self.druid.say_dialogue("A light reading, does no harm"))
        time.sleep(1)
        print(self.druid.say_dialogue(f"Now {self.player.name}, Lets begin with Challenge 2!"))
        game.book_roulette()

    #




    def DruidQuarter(self):
            self.current_location = self.sublocation[3]
            print(f"Location: {self.current_location}")
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
                    print(self.druid.say_dialogue("I knew this day would come!, but before you begin you must prove to me that you are capable to embark on this quest!"))
                    print(self.druid.say_dialogue("It will test your mental, physical and quick thinking abilities!"))
                    print(self.druid.say_dialogue("Let us Begin! - with a quick riddle!"))
                    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"

                    print(f"Riddle: {riddle}")
                    while True:
                        # Get the player's answer
                        player_answer = input("Your answer: ").lower()

                        # Check if the player's answer is correct
                        if player_answer == "an echo":
                            print("Congratulations! You've solved the Riddle! - Here is 3 coins")
                            self.player.coins = self.player.coins + 3
                            print(f"YOUR CURRENT COINS: {self.player.coins}")
                            break;
                            print("Lets head to the library for your next challenge")
                            break
                            GrandLibrary()
                        else:
                            print(f"{self.druid.name: looks doubtful...}")
                            print("Unfortunately, that's not the correct answer. Keep trying!")

                else:
                    print(self.druid.say_dialogue("Maybe I had made a mistake in summoning you..."))
                    print("\nYou must complete the Druid's Activities to continue further in this level!")








if __name__ == "__main__":
    player = Player("Player Name")
    player.coins = 0
    level1 = Level1(player, 0)  # Pass the player object to Level1 constructor
    level1.GameIntro()
    level1.HallOfWarriors()  # Call the method on the instance
