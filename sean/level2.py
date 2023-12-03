from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player
from sean.fight import fight, User, RedCloakEnemy
from sean.dice_game import roll_dice
from sean.colour_puzzle import ColoredSlabPuzzle

import time


class Level2(Location):
    def __init__(self, player):
        super().__init__("City",
                         ["Outside City Walls", "Barbarian Group",
                          "Dark Alley", "Back City Walls",
                          "Around City Walls", "City Streets"],
                         ["City Guard", "Barbarian", "Red Cloak Man"],
                         [])
        self.current_location = self.sublocation[0]
        self.player = player
        self.city_guard = NPC("City Guard",
                              ["Halt! What business do "
                               "you have here stranger?",
                               "Kidnapping you say? Haven't "
                               "heard anything about that. Although I did "
                               "oversee some sketchy figures talking nearby",
                               "You already asked me about the "
                               "kidnappings",
                               "Ah, I see you have a city pass",
                               "You may proceed stranger",
                               "Hold! You can't enter without a "
                               "city pass",
                               "Safe travels, stranger"
                               ],
                              "City guard saw some shady characters talking "
                              "near the "
                              "city gates.",
                              "",
                              "")
        self.barbarian = NPC("Barbarian Leader",
                             ["Looky here boys! Some fresh meat",
                              "I am in need of something as well. Perhaps we "
                              "can strike a deal..",
                              "You retrieve my prized dagger and I offer you "
                              "our services. What say you?",
                              "Wonderful. My dagger was stolen by a man in a "
                              "red cloak.\n"
                              "I think I saw him head around the back of the "
                              "city",
                              "Off ya hop now fresh meat and don't come back "
                              "without my dagger!",
                              "Stop wasting my time then! Scram!",
                              "You have returned. With my prized dagger I "
                              "hope?",
                              "Hold on now, I also want some gold from you. "
                              "You look as though you have a bit to spare",
                              "I don't remember no deal. Do you boys?",
                              "That's what I like to hear, get 'em boys!",
                              "Suit yourself. Thanks for the dagger",
                              "Return with the dagger or not at all!",
                              "Want to take me up on my offer now?",
                              "See that wasn't so hard. My dagger was stolen "
                              "by a man in a red cloak.\n I think I saw him "
                              "head around the back of the city",
                              "Off ya hop now fresh meat and don't come "
                              "back without my dagger!",
                              "Why do you keep approaching me then?!"],
                             "The barbarian's prized dagger was stolen by a "
                             "man in a red cloak",
                             "",
                             "")
        self.red_cloak_man = NPC("Red Cloaked Figure",
                                 ["What do we have here?",
                                  "You'll have to win it fair and square",
                                  "I'll play you in a game of dice for it",
                                  "Back off stranger! This is mine! I found "
                                  "it!",
                                  "I told you to back off! My precious!",
                                  "You'll have to win it off me in dice then\n"
                                  "and i never lose in dice!",
                                  "So this is how it'll be"],
                                 "",
                                 "Prized Dagger",
                                 "")

        # Boolean variable set for no double interaction with the city guard
        self.__guard_interacted = False
        self.__guard_asked = False
        self.__barbarians_asked = False
        self.__deal_made = False
        self.__deal_complete = False
        self.__cloak_figure_interact = False
        self.__cloak_figure_fin = False
        self.__dark_alley_investigated = False
        self.puzzle_complete = False

    def level_start(self):
        self.outside_city()

    def outside_city(self):
        self.current_location = self.sublocation[0]
        print(f"{self.current_location} - "
              f"The coldness of the night creeps into your soul.\n"
              f"You see the silhouette of the towering city gates ahead of "
              f"you, guarded by vigilant city guards.")

        time.sleep(2)

        while True:
            action = input("\nWhat will you do?\n"
                           "1) Approach the city gates\n"
                           "2) Explore Around the City Walls\n"
                           "3) Check the immediate area\n")

            if action == "1":
                self.guard_interaction()
            elif action == "2":
                self.explore_surroundings()
            elif action == "3":
                print("\nYou look around to see if there is a way to get into "
                      "the city.\n")
                time.sleep(1)
                self.barbarian_camp()

            if self.current_location == self.sublocation[5]:
                print(f"You have entered the city! You are now in the "
                      f"{self.current_location}.")
                time.sleep(1)
                print("The hustle and bustle of the city's inhabitants "
                      "surrounds you.")
                print(self.view_visited_locations())
                break  # Exit the loop once the player enters the city

    def guard_interaction(self):
        print(self.city_guard.say_dialogue(self.city_guard.dialogue[0]), "\n")

        while not self.__guard_interacted:
            interaction = int(input("1) Ask about the kidnapping\n"
                                    "2) Ask if you can get by\n"
                                    "3) Leave the city gates\n"))

            if interaction == 1:
                if not self.__guard_asked:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[1]), "\n")
                    time.sleep(1)
                    self.add_clue(self.city_guard.clue())
                    self.__guard_asked = True
                else:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[2]), "\n")
                    time.sleep(1)
            elif interaction == 2:
                if "City Pass" in self.player.inventory:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[3]), "\n")
                    time.sleep(1)
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[4]), "\n")
                    time.sleep(1)
                    self.current_location = self.sublocation[5]
                    self.__guard_interacted = True
                else:
                    print(self.city_guard.say_dialogue
                          (self.city_guard.dialogue[5]), "\n")
                    time.sleep(1)
            elif interaction == 3:
                print(self.city_guard.say_dialogue
                      (self.city_guard.dialogue[6]))
                time.sleep(1)
                break

    def explore_surroundings(self):
        self.current_location = self.sublocation[3]
        print("\nYou notice a dark alley at the back of the city walls\n")
        time.sleep(2)
        exploration_result = input("1) Investigate the dark alley\n"
                                   "2) Examine the back of the city "
                                   "walls\n"
                                   "3) Return to the city gates\n")

        if exploration_result == "1":
            self.current_location = self.sublocation[2]
            self.dark_alley()

        elif exploration_result == "2":
            if not self.__cloak_figure_fin:
                self.visited("Back City Walls")
                print("\nYou examine the back of the city walls.\n")
                time.sleep(1)
                if self.__deal_made and not self.__cloak_figure_interact:
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something")
                    time.sleep(2)
                    print("\nYou notice that this is the man the barbarian "
                          "was talking about.")
                    time.sleep(1)
                    print("\nYou see the prized dagger in his hand")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[0]), "\n")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I'll be needing that dagger\n")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[1]), "\n")
                    time.sleep(1)
                    if 'Chaos Sword' in self.player.inventory:
                        print(self.red_cloak_man.say_dialogue
                              (self.red_cloak_man.dialogue[2]), "\n")
                        cloaked_figure_option = input("Do you want to fight "
                                                      "him for it or play "
                                                      "his little game?"
                                                      "1) Fight him!"
                                                      "2) Game time!")
                        if cloaked_figure_option == "1":
                            print(f"{self.player.name}:\n Give it to me\n")
                            time.sleep(1)
                            user = User(self.player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                        elif cloaked_figure_option == "2":
                            print(f"{self.player.name}:\n Let's play then\n")
                            time.sleep(1)
                            prize = roll_dice()
                            if prize:
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                    else:
                        print(self.red_cloak_man.say_dialogue
                              (self.red_cloak_man.dialogue[2]), "\n")
                        time.sleep(1)
                        print(f"{self.player.name}:\n Let's play then\n")
                        time.sleep(1)
                        prize = roll_dice()
                        if prize:
                            self.player.add_item(prize)
                            self.player.show_inventory()
                            print("You gained 25 coins from "
                                  "beating him.")
                            self.player.coins += 25
                        self.__cloak_figure_fin = True

                elif not self.__deal_made and not self.__cloak_figure_interact:
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something.\n")
                    time.sleep(2)
                    print("You approach the man to ask if there is a way in.")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[0]), "\n")
                    time.sleep(1)
                    print("He seems deep in admiration to what he is holding "
                          "but notices you when you get closer.")
                    time.sleep(2)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[3]), "\n")
                    time.sleep(1)
                    print("You back off slowly. You don't want to get into "
                          "any unnecessary trouble.")
                    time.sleep(1)
                    self.__cloak_figure_interact = True

                elif self.__deal_made and self.__cloak_figure_interact:
                    print("You come back to the cloaked man.")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[4]), "\n")
                    time.sleep(1)
                    print("You notice now that this is the man the barbarian "
                          "was talking about.")
                    time.sleep(1)
                    print("You see the prized dagger in his hand.")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I'll be needing that dagger.\n")
                    time.sleep(1)
                    print(self.red_cloak_man.say_dialogue
                          (self.red_cloak_man.dialogue[5]), "\n")
                    time.sleep(1)
                    if 'Chaos Sword' in self.player.inventory:
                        cloaked_figure_option = input("Play his little dice "
                                                      "game or rip it from "
                                                      "his cold dead hands?"
                                                      "1) Fight him!"
                                                      "2) Game time!")
                        if cloaked_figure_option == "1":
                            print(f"{self.player.name}:\n I'll be taking that "
                                  f"dagger.\n")
                            time.sleep(1)
                            print(self.red_cloak_man.say_dialogue
                                  (self.red_cloak_man.dialogue[6]), "\n")
                            time.sleep(1)
                            user = User(self.player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                        elif cloaked_figure_option == "2":
                            print(f"{self.player.name}:\n Let's play then.\n")
                            time.sleep(1)
                            prize = roll_dice()
                            if prize:
                                self.player.add_item(prize)
                                self.player.show_inventory()
                                print("You gained 25 coins from "
                                      "beating him.")
                                self.player.coins += 25
                            self.__cloak_figure_fin = True
                    else:
                        print(f"{self.player.name}:\n Let's play then.\n")
                        time.sleep(1)
                        prize = roll_dice()
                        if prize:
                            self.player.add_item(prize)
                            self.player.show_inventory()
                            print("You gained 25 coins from "
                                  "beating him.")
                            self.player.coins += 25
                        self.__cloak_figure_fin = True
                else:
                    print("You dont want to cause any trouble so you stay "
                          "away from the cloaked figure.\n")
                    time.sleep(2)
            else:
                print("You lost and can't get the prized dagger now.\n"
                      "You'll have to find another way into the city\n")
                time.sleep(2)

        elif exploration_result == "3":
            print("You decide to return to the city gates.\n")
            time.sleep(1)

        else:
            print("Invalid option.\n")

    def barbarian_camp(self):

        self.current_location = self.sublocation[1]
        if "Barbarian Group" not in self.visited_sublocations:
            self.visited("Barbarian Group")

        if not self.__barbarians_asked:
            barbarian_option = input("1) Look for a distraction\n"
                                     "2) Return to the previous "
                                     "options\n")

            if barbarian_option == "1":
                print("While scanning the surroundings, you notice a "
                      "group of barbarians nearby.\n")
                time.sleep(2)
                print("The barbarians seem rowdy but open to negotiation.\n")
                time.sleep(1)
                approach_barbarians = input("Do you want to approach them?\n"
                                            "1) Yes, approach the barbarians\n"
                                            "2) No, return to the previous "
                                            "options\n")

                if approach_barbarians == "1":
                    print("You approach the barbarians cautiously.\n")
                    time.sleep(1)
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[0]), "\n")
                    time.sleep(1)
                    print(f"{self.player.name}:\n I need a distraction to get into "
                          f"the city, it's very important.\n")
                    time.sleep(2)
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[1]), "\n")
                    time.sleep(2)
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[2]), "\n")
                    time.sleep(2)
                    deal_option = input("Do you want to strike a deal with "
                                        "the barbarian?\n"
                                        "1) Yes, what could go wrong?\n"
                                        "2) Hell no!\n")
                    if deal_option == "1":
                        print("\n")
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[3]), "\n")
                        time.sleep(1)
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[4]), "\n")
                        time.sleep(1)
                        self.__deal_made = True
                        self.add_clue(self.barbarian.clue())
                    elif deal_option == "2":
                        print("\n")
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[5]), "\n")
                        time.sleep(1)
                    self.__barbarians_asked = True
                elif approach_barbarians == "2":
                    print("You decide not to approach the barbarians and "
                          "look for alternative options.\n")
                    time.sleep(1)

            elif barbarian_option == "2":
                print("You decide to return to the previous options.\n")
                time.sleep(1)

            else:
                print("Invalid option.\n")

        else:
            barbarian_option = input("1) Return to the barbarians\n"
                                     "2) Return to the previous options\n")

            if self.__deal_made:
                if barbarian_option == "1" and not self.__deal_complete:
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[6]), "\n")
                    time.sleep(1)
                    if "Prized Dagger" in self.player.inventory:
                        print(f"{self.player.name}:\n Yes I have, now can you "
                              f"create a distraction for me?\n")
                        time.sleep(1)
                        print("You give him his oh so special dagger.\n")
                        time.sleep(2)
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[7]), "\n")
                        time.sleep(1)
                        print(f"{self.player.name}:\n That wasn't the deal.\n")
                        time.sleep(1)
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[8]), "\n")
                        time.sleep(2)
                        print("They all reply in unison: No!\n")
                        time.sleep(1)
                        if self.player.coins >= 20:
                            print(f"You have {self.player.coins} coins.\n")
                            distraction = input("Do you wish to give the "
                                                "barbarians some coin(20) to "
                                                "create the distraction?\n"
                                                "1) Yes\n"
                                                "2) No")
                            if distraction == "1":
                                print(f"{self.player.name}:\n Fine, I do really "
                                      f"need to get in there.\n")
                                time.sleep(1)
                                print(self.barbarian.say_dialogue
                                      (self.barbarian.dialogue[9]), "\n")
                                time.sleep(1)
                                print("They all rush towards the city gates, "
                                      "charging the guards that block the"
                                      "entrance.\n")
                                time.sleep(2)
                                print("With the distraction in place, you "
                                      "slip past the guards and enter the "
                                      "city.\n")
                                time.sleep(2)
                                self.__guard_interacted = True
                                self.current_location = self.sublocation[5]
                                self.player.coins -= 20
                            elif distraction == "2":
                                print(f"{self.player.name}:\n Forget it then. "
                                      f"I'll find my own way in.\n")
                                time.sleep(1)
                                print(self.barbarian.say_dialogue
                                      (self.barbarian.dialogue[10]), "\n")
                                time.sleep(1)
                                print("You hear them all cackling as you "
                                      "walk away.\n")
                                time.sleep(1)
                                self.__deal_complete = True
                        else:
                            print("You don't have enough coins to bribe the "
                                  "barbarians.")
                            print("You decide to explore other options.\n")
                            time.sleep(1)
                    else:
                        print(self.barbarian.say_dialogue
                              (self.barbarian.dialogue[11]), "\n")
                        time.sleep(1)

                elif barbarian_option == "1" and self.__deal_complete:
                    print("You got scammed by the barbarians and made a fool "
                          "of. You decide not to go back to them.\n")
                    time.sleep(2)

                elif barbarian_option == "2":
                    print("You decide to return to the previous options.\n")
                    time.sleep(1)

                else:
                    print("Invalid option.\n")
            else:
                print(self.barbarian.say_dialogue
                      (self.barbarian.dialogue[12]), "\n")
                time.sleep(1)
                deal_option = input("1) Yes, what could go wrong?\n"
                                    "2) Hell no!\n")
                if deal_option == "1":
                    print("\n")
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[13]), "\n")
                    time.sleep(1)
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[14]), "\n")
                    time.sleep(1)
                    self.__deal_made = True
                    self.add_clue(self.barbarian.clue())
                elif deal_option == "2":
                    print("\n")
                    print(self.barbarian.say_dialogue
                          (self.barbarian.dialogue[15]), "\n")
                    time.sleep(1)

    def dark_alley(self):
        print("You decide to investigate the dark alley.\n")
        if self.current_location not in self.visited_sublocations:
            print("As you enter the narrow alley, you hear a faint sound.\n")
            self.visited(self.sublocation[2])

        while self.current_location == self.sublocation[2]:
            event_result = input("1) Follow the sound\n"
                                 "2) Go deeper into the alley\n"
                                 "3) Leave the alley\n")

            if event_result == "1":
                if not self.__dark_alley_investigated:
                    print("You follow the sound and discover a hidden door.\n")
                    time.sleep(1)
                    print("Behind the door, you find a group of hooded "
                          "figures planning a secret meeting.\n")
                    time.sleep(2)
                    print("They are dressed in red, blue and yellow robes.\n")
                    time.sleep(1)
                    print("They almost notice you, but you were able to slip "
                          "away before they caught you.\n")
                    time.sleep(2)

                    self.add_clue("secret meeting under city")
                    self.add_clue("figures in blue, red and yellow robes")
                    self.__dark_alley_investigated = True
                else:
                    print("You don't want to go back there, they might see "
                          "you.\n")
                    time.sleep(1)

            elif event_result == "2":
                if not self.puzzle_complete:
                    print("You find a pile of coloured slabs and 3 slots that "
                          "they seem to fit into.\n")
                    time.sleep(2)
                    colored_slab_puzzle = ColoredSlabPuzzle(self.review_clues())
                    city_pass = colored_slab_puzzle.play_puzzle()
                    if city_pass:
                        self.player.add_item(city_pass)
                        self.player.show_inventory()
                    self.puzzle_complete = True
                else:
                    print("You've already completed the puzzle in this "
                          "area.\n")
                    time.sleep(1)

            elif event_result == "3":
                print("You decide to leave the dark alley.")
                time.sleep(1)
                self.current_location = self.sublocation[4]
                break

            else:
                print("Invalid option.\n")


if __name__ == "__main__":
    player = Player("Player Name")
    level2 = Level2(player)

    level2.outside_city()
