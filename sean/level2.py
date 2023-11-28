from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player


# Get city pass from puzzle when you examine back city walls


class Level2(Location):
    def __init__(self, score):
        super().__init__("City",
                         ["Outside City Walls", "Barbarian Group",
                          "Dark Alley", "Back City Walls",
                          "Around City Walls", "City Streets"],
                         ["City Guard", "Barbarian"],
                         [])
        self.current_location = self.sublocation[0]
        self.player = player
        self.score = score
        self.city_guard = NPC("City Guard:",
                              "Halt! What business do you have here "
                              "stranger?",
                              "Overheard some shady characters talking near "
                              "the city gates.",
                              "")
        self.barbarian = NPC("Barbarian Leader:",
                             "Looky here boys! Some fresh meat",
                             "The barbarian's prized dagger was stolen by a thief",
                             "")

        # Boolean variable set for no double interaction with the city guard
        self.__guard_interacted = False
        self.__guard_asked = False
        self.__barbarians_asked = False
        self.__dark_alley_investigated = False

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
                if not self.__guard_interacted:
                    print(self.city_guard.interact())

                    while not self.__guard_interacted:
                        interaction = int(input("1) Ask about the kidnapping\n"
                                                "2) Ask if you can get by\n"
                                                "3) Leave the city gates\n"))

                        if interaction == 1:
                            if not self.__guard_asked:
                                print(self.city_guard)
                                print(self.city_guard.say_dialogue(f"Kidnapping "
                                                                   f"you say? "
                                                                   f"Haven't "
                                                                   f"heard "
                                                                   f"anything "
                                                                   f"about that. "
                                                                   f"Although I "
                                                                   f"did oversee "
                                                                   f"some shady "
                                                                   f"figures "
                                                                   f"talking "
                                                                   f"nearby"))
                                self.add_clue(self.city_guard.clue())
                                self.__guard_asked = True
                            else:
                                print(self.city_guard.say_dialogue("You already asked me about the kidnappings"))
                        elif interaction == 2:
                            if "City Pass" in self.player.inventory:
                                print(self.city_guard.say_dialogue("Oh, you have a city pass. "
                                      "You may proceed. Stay safe!"))
                                self.__guard_interacted = True
                            else:
                                print(self.city_guard.say_dialogue("Hold! You can't enter "
                                      "without a city pass."))
                        elif interaction == 3:
                            print(self.city_guard.say_dialogue("Safe travels, stranger."))
                else:
                    print("You already interacted with the city guard.")
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

    def explore_surroundings(self):
        self.current_location = self.sublocation[3]
        print("You notice a dark alley at the back of the city walls")
        exploration_result = input("1) Investigate the dark alley\n"
                                   "2) Examine the back of the city "
                                   "walls\n"
                                   "3) Return to the city gates\n")

        if exploration_result == "1":
            self.current_location = self.sublocation[2]
            if self.current_location not in self.visited_sublocations:
                self.dark_alley(self.current_location)
            else:
                print("You have already visited the dark alley.")

        elif exploration_result == "2":
            self.visited("Back City Walls")
            print("You examine the back of the city walls.")
            self.player.add_item("Prized Dagger")
            # Add puzzle logic or other events related to examining the
            # city walls (to be implemented later)

        elif exploration_result == "3":
            print("You decide to return to the city gates.")

        else:
            print("Invalid option.")

    def barbarian_camp(self):

        distraction_option = input("1) Look for a distraction\n"
                                   "2) Return to the previous "
                                   "options\n")

        if distraction_option == "1":
            print("While scanning the surroundings, you notice a "
                  "group of barbarians nearby.")

            self.current_location = self.sublocation[1]

            bribe_option = input("The barbarians seem rowdy but open "
                                 "to negotiation.\n"
                                 "Do you want to approach them?\n"
                                 "1) Yes, approach the barbarians\n"
                                 "2) No, return to the previous "
                                 "options\n")

            if bribe_option == "1":
                print("You approach the barbarians cautiously")
                if not self.__barbarians_asked:
                    print(self.barbarian.interact())
                    print(f"{player.name}: I need a distraction to get into the city, it's very important.")
                    print(self.barbarian.say_dialogue("I am in need of something as well.\n"
                                                      "Perhaps we can strike a deal.."))
                    print(self.barbarian.say_dialogue("You retrieve my prized dagger\n"
                                                      "and I offer you our services. What say you?"))
                    self.add_clue(self.barbarian.clue())
                    self.__barbarians_asked = True
                else:
                    print(self.barbarian.say_dialogue("You have returned. With my prized dagger I hope?"))
                    if "Prized Dagger" in self.player.inventory:
                        print("Yes")
                        if self.player.coins >= 25:
                            print("With the distraction in place, you slip "
                                  "past the guards and enter the city.")
                            self.visited("Barbarian Group")
                            self.__guard_interacted = True
                            self.current_location = self.sublocation[5]
                            self.player.coins -= 25
                        else:
                            print("You don't have enough coins to bribe the "
                                  "barbarians.")
                            print("You decide to explore other options.")
                    else:
                        print(self.barbarian.say_dialogue("Return with the dagger or not at all!"))
            elif bribe_option == "2":
                print("You decide not to approach the barbarians and "
                      "look for alternative options.")
            else:
                print("Invalid option.")
        elif distraction_option == "2":
            print("You decide to return to the previous options.")

        else:
            print("Invalid option.")

    def dark_alley(self, location):
        print("You decide to investigate the dark alley.")
        print("As you enter the narrow alley, you hear a faint sound.")

        while location == self.sublocation[2]:
            event_result = input("1) Follow the sound\n"
                                 "2) Go deeper into the alley\n"
                                 "3) Leave the alley\n")

            if event_result == "1":
                print("You follow the sound and discover a hidden door.")
                print("Behind the door, you find a group of hooded "
                      "figures planning a secret meeting.")
                print("They almost notice you, but you were able to slip "
                      "away before they caught you.")

                self.add_clue("secret meeting under city")
                self.__dark_alley_investigated = True
                self.visited(self.sublocation[2])

            elif event_result == "2":
                print("You decide to go deeper into the alley.")
                print("After navigating through the narrow passages, "
                      "you find yourself at the bottom of a well.")
                print("You climb up and find yourself inside the city "
                      "walls.")
                self.visited(self.sublocation[2])
                self.current_location = self.sublocation[5]

            elif event_result == "3":
                print("You decide to leave the dark alley.")
                self.visited(self.sublocation[2])
                self.current_location = self.sublocation[4]
                break

            else:
                print("Invalid option.")


if __name__ == "__main__":
    player = Player("Player Name")
    player.coins = 25
    level2 = Level2(player)

    level2.outside_city()
