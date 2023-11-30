from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player
from sean.fight import fight, User, RedCloakEnemy
from sean.dice_game import roll_dice
from sean.colour_puzzle import ColoredSlabPuzzle


# change dark alley to


class Level2(Location):
    def __init__(self, score):
        super().__init__("City",
                         ["Outside City Walls", "Barbarian Group",
                          "Dark Alley", "Back City Walls",
                          "Around City Walls", "City Streets"],
                         ["City Guard", "Barbarian", "Red Cloak Man"],
                         [])
        self.current_location = self.sublocation[0]
        self.player = player
        self.score = score
        self.city_guard = NPC("City Guard",
                              ["City Guard: Halt! What business do "
                               "you have here stranger?",
                               "City Guard: Kidnapping you say? Haven't "
                               "heard anything about that. Although I did "
                               "oversee some sketchy figures talking nearby",
                               "City Guard: You already asked me about the "
                               "kidnappings",
                               "City Guard: You may proceed stranger",
                               "City Guard: Hold! You can't enter without a "
                               "city pass",
                               "City Guard: Safe travels, stranger"
                               ],
                              "City guard saw some shady characters talking "
                              "near the "
                              "city gates.",
                              "",
                              "")
        self.barbarian = NPC("Barbarian Leader",
                             "Looky here boys! Some fresh meat",
                             "The barbarian's prized dagger was stolen by a "
                             "man in a red cloak",
                             "",
                             "")
        self.red_cloak_man = NPC("Red Cloaked Figure",
                                 "What do we have here?",
                                 "",
                                 "Prized Dagger",
                                 "")

        # Boolean variable set for no double interaction with the city guard
        self.__guard_interacted = False
        self.__guard_asked = False
        self.__barbarians_asked = False
        self.__deal_made = False
        self.__cloak_figure_interact = False
        self.__cloak_figure_fin = False
        self.__dark_alley_investigated = False
        self.puzzle_complete = False

    def outside_city(self):
        self.current_location = self.sublocation[0]
        print(f"{self.current_location} - "
              f"The coldness of the night creeps into your soul.\n"
              f"You see the silhouette of the towering city gates ahead of "
              f"you, guarded by vigilant city guards.")

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
                print("You look around to see if there is a way to get into "
                      "the city.")
                self.barbarian_camp()

            if self.current_location == self.sublocation[5]:
                print(f"You have entered the city! You are now in the "
                      f"{self.current_location}.")
                print("The hustle and bustle of the city's inhabitants "
                      "surrounds you.")
                print(self.view_visited_locations())
                break  # Exit the loop once the player enters the city

    def guard_interaction(self):
        print(self.city_guard._dialogue[0])

        while not self.__guard_interacted:
            interaction = int(input("1) Ask about the kidnapping\n"
                                    "2) Ask if you can get by\n"
                                    "3) Leave the city gates\n"))

            if interaction == 1:
                if not self.__guard_asked:
                    print(self.city_guard)
                    print(self.city_guard._dialogue[1])
                    self.add_clue(self.city_guard.clue())
                    self.__guard_asked = True
                else:
                    print(self.city_guard._dialogue[2])
            elif interaction == 2:
                if "City Pass" in self.player.inventory:
                    print(self.city_guard._dialogue[3])
                    self.current_location = self.sublocation[5]
                    self.__guard_interacted = True
                else:
                    print(self.city_guard._dialogue[4])
            elif interaction == 3:
                print(self.city_guard._dialogue[5])
                break

    def explore_surroundings(self):
        self.current_location = self.sublocation[3]
        print("You notice a dark alley at the back of the city walls")
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
                print("You examine the back of the city walls.")
                if self.__deal_made and not self.__cloak_figure_interact:
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something")
                    print("You notice that this is the man the barbarian was "
                          "talking about.")
                    print("You see the prized dagger in his hand")
                    print(f"{player.name} I'll be needing that dagger")
                    print(self.red_cloak_man.say_dialogue("You'll have to "
                                                          "win it fair and "
                                                          "square"))
                    if "Sword" in player.inventory:
                        print(self.red_cloak_man.say_dialogue("I'll play you "
                                                              "in a game of "
                                                              "dice for it"))
                        cloaked_figure_option = input("Do you want to fight "
                                                      "him for it or play "
                                                      "his little game?"
                                                      "1) Fight him!"
                                                      "2) Game time!")
                        if cloaked_figure_option == "1":
                            print(f"{player.name}: Give it to me")
                            user = User(player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                player.add_item(prize)
                                player.show_inventory()
                            self.__cloak_figure_fin = True
                        elif cloaked_figure_option == "2":
                            print(f"{player.name}: Let's play then")
                            prize = roll_dice()
                            if prize:
                                player.add_item(prize)
                                player.show_inventory()
                            self.__cloak_figure_fin = True
                    else:
                        print(self.red_cloak_man.say_dialogue("I'll play you "
                                                              "in a game of "
                                                              "dice for it"))
                        print(f"{player.name}: Let's play then")
                        prize = roll_dice()
                        if prize:
                            player.add_item(prize)
                            player.show_inventory()
                        self.__cloak_figure_fin = True

                elif not self.__deal_made and not self.__cloak_figure_interact:
                    print("You see a figure hiding at the back of the city "
                          "walls.\n"
                          "They are dressed in a red cloak and look to be "
                          "trying to hide something")
                    print("You approach the man to ask if there is a way in")
                    print(self.red_cloak_man.interact())
                    print("He seems deep in admiration to what he is holding "
                          "but notices you when you get closer")
                    print(self.red_cloak_man.say_dialogue("Back off "
                                                          "stranger! This is"
                                                          " mine! I found "
                                                          "it!"))
                    print("You back off slowly. You don't want to get into "
                          "any unnecessary trouble")
                    self.__cloak_figure_interact = True

                elif self.__deal_made and self.__cloak_figure_interact:
                    print("You come back to the cloaked man.")
                    print(self.red_cloak_man.say_dialogue("I told you to "
                                                          "back off! My "
                                                          "precious!"))
                    print("You notice now that this is the man the barbarian "
                          "was talking about.")
                    print("You see the prized dagger in his hand")
                    print(f"{player.name} I'll be needing that dagger")
                    print(self.red_cloak_man.say_dialogue("You'll have to "
                                                          "win it off me in "
                                                          "dice then\n"
                                                          "and i never lose "
                                                          "in dice!"))
                    if "Sword" in player.inventory:
                        cloaked_figure_option = input("Play his little dice "
                                                      "game or rip it from "
                                                      "his cold dead hands?"
                                                      "1) Fight him!"
                                                      "2) Game time!")
                        if cloaked_figure_option == "1":
                            print(f"{player.name} I'll be taking that dagger")
                            print(self.red_cloak_man.say_dialogue("So this "
                                                                  "is how "
                                                                  "it'll be"))
                            user = User(player.name)
                            red_cloak = RedCloakEnemy()
                            prize = fight(user, red_cloak)
                            if prize:
                                player.add_item(prize)
                                player.show_inventory()
                            self.__cloak_figure_fin = True
                        elif cloaked_figure_option == "2":
                            print(f"{player.name} Let's play then")
                            prize = roll_dice()
                            if prize:
                                player.add_item(prize)
                                player.show_inventory()
                            self.__cloak_figure_fin = True
                    else:
                        print(f"{player.name} Let's play then")
                        prize = roll_dice()
                        if prize:
                            player.add_item(prize)
                            player.show_inventory()
                        self.__cloak_figure_fin = True
                else:
                    print("You dont want to cause any trouble so you stay "
                          "away from the cloaked figure.")
            else:
                print("You lost and can't get the prized dagger now.\n"
                      "You'll have to find another way into the city")

        elif exploration_result == "3":
            print("You decide to return to the city gates.")

        else:
            print("Invalid option.")

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
                      "group of barbarians nearby.")

                approach_barbarians = input("The barbarians seem rowdy but "
                                            "open to negotiation.\n"
                                            "Do you want to approach them?\n"
                                            "1) Yes, approach the barbarians\n"
                                            "2) No, return to the previous "
                                            "options\n")

                if approach_barbarians == "1":
                    print("You approach the barbarians cautiously")
                    print(self.barbarian.interact())
                    print(f"{player.name}: I need a distraction to get into "
                          f"the city, it's very important.")
                    print(self.barbarian.say_dialogue("I am in need of "
                                                      "something as well."
                                                      "Perhaps we can strike "
                                                      "a deal.."))
                    print(self.barbarian.say_dialogue("You retrieve my "
                                                      "prized dagger"
                                                      "and I offer you our "
                                                      "services. What say "
                                                      "you?"))
                    deal_option = input("Do you want to strike a deal with "
                                        "the barbarian?\n"
                                        "1) Yes, what could go wrong?\n"
                                        "2) Hell no!\n")
                    if deal_option == "1":
                        print(self.barbarian.say_dialogue("Wonderful. My "
                                                          "dagger was stolen "
                                                          "by a man in a red "
                                                          "cloak."
                                                          "I think I saw him "
                                                          "head around the "
                                                          "back of the city"))
                        print(self.barbarian.say_dialogue("Off ya hop now "
                                                          "fresh meat and "
                                                          "don't come back"
                                                          "without my "
                                                          "dagger!"))
                        self.__deal_made = True
                        self.add_clue(self.barbarian.clue())
                    elif deal_option == "2":
                        print(self.barbarian.say_dialogue("Stop wasting my "
                                                          "time then! Scram!"))
                    self.__barbarians_asked = True
                elif approach_barbarians == "2":
                    print("You decide not to approach the barbarians and "
                          "look for alternative options.")

            elif barbarian_option == "2":
                print("You decide to return to the previous options.")

            else:
                print("Invalid option.")

        else:
            barbarian_option = input("1) Return to the barbarians\n"
                                     "2) Return to the previous options\n")

            if self.__deal_made:
                if barbarian_option == "1":
                    print(self.barbarian.say_dialogue("You have returned. "
                                                      "With my prized dagger"
                                                      " I hope?"))
                    if "Prized Dagger" in self.player.inventory:
                        print("Yes")
                        if self.player.coins >= 25:
                            print("With the distraction in place, you slip "
                                  "past the guards and enter the city.")
                            self.__guard_interacted = True
                            self.current_location = self.sublocation[5]
                            self.player.coins -= 25
                        else:
                            print("You don't have enough coins to bribe the "
                                  "barbarians.")
                            print("You decide to explore other options.")
                    else:
                        print(self.barbarian.say_dialogue("Return with the "
                                                          "dagger or not at "
                                                          "all!"))

                elif barbarian_option == "2":
                    print("You decide to return to the previous options.")

                else:
                    print("Invalid option.")
            else:
                print(self.barbarian.say_dialogue("Want to take me up on my "
                                                  "offer now?"))
                deal_option = input("1) Yes, what could go wrong?\n"
                                    "2) Hell no!\n")
                if deal_option == "1":
                    print(self.barbarian.say_dialogue("See that wasn't so "
                                                      "hard. My dagger was "
                                                      "stolen by a man in a"
                                                      "red cloak.\nI think I "
                                                      "saw him head around "
                                                      "the back of the city"))
                    print(self.barbarian.say_dialogue("Off ya hop now fresh "
                                                      "meat and don't come "
                                                      "back without my "
                                                      "dagger!"))
                    self.__deal_made = True
                    self.add_clue(self.barbarian.clue())
                elif deal_option == "2":
                    print(self.barbarian.say_dialogue("Why do you keep "
                                                      "approaching me then?!"))

    def dark_alley(self):
        print("You decide to investigate the dark alley.")
        if self.current_location not in self.visited_sublocations:
            print("As you enter the narrow alley, you hear a faint sound.")
            self.visited(self.sublocation[2])

        while self.current_location == self.sublocation[2]:
            event_result = input("1) Follow the sound\n"
                                 "2) Go deeper into the alley\n"
                                 "3) Leave the alley\n")

            if event_result == "1":
                if not self.__dark_alley_investigated:
                    print("You follow the sound and discover a hidden door.")
                    print("Behind the door, you find a group of hooded "
                          "figures planning a secret meeting.")
                    print("They are dressed in red, blue and yellow robes")
                    print("They almost notice you, but you were able to slip "
                          "away before they caught you.")

                    self.add_clue("secret meeting under city")
                    self.add_clue("figures in blue, red and yellow robes")
                    self.__dark_alley_investigated = True
                else:
                    print("You don't want to go back there, they might see "
                          "you")

            elif event_result == "2":
                if not self.puzzle_complete:
                    print("You find a pile of coloured slabs and 3 slots that "
                          "they seem to fit into")
                    colored_slab_puzzle = ColoredSlabPuzzle(level2)
                    city_pass = colored_slab_puzzle.play_puzzle()
                    if city_pass:
                        player.add_item(city_pass)
                        player.show_inventory()
                    self.puzzle_complete = True
                else:
                    print("You've already completed the puzzle in this area.")

            elif event_result == "3":
                print("You decide to leave the dark alley.")
                self.current_location = self.sublocation[4]
                break

            else:
                print("Invalid option.")


if __name__ == "__main__":
    player = Player("Player Name")
    level2 = Level2(player)

    level2.outside_city()
