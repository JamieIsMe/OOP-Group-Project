from cian.characters import NPC
from sean.locationClass import Location
from denis.Player import Player


class Level2(Location):
    def __init__(self, score):
        super().__init__("City", "Outside City Walls", [], [])
        self.current_location = "entrance to the city"
        self.player = player
        self.score = score
        self.visited_locations = []
        self.city_guard = NPC("City Guard",
                              "Halt! What business do you have here, stranger?",
                              "Overheard some shady characters talking near the city gates.",
                              "City Map")

        # Boolean variable set for no double interaction with the city guard
        self.__guard_interacted = False

        self.__dark_alley_investigated = False

    def outside_city(self):
        print(f"{self.current_location.capitalize()} - A cold night outside the city walls.\n"
              f"You see the silhouette of the towering city gates ahead of you, guarded by vigilant city guards.")

        while self.current_location == "entrance to the city":
            action = input("\nWhat will you do?\n"
                           "1) Approach the city gates\n"
                           "2) Explore the surroundings\n"
                           "3) Check the immediate area\n")

            if action == "1":
                if not self.__guard_interacted:
                    print(self.city_guard.interact())

                    while not self.__guard_interacted:
                        interaction = int(input("1) Ask about the kidnapping\n"
                                                "2) Ask if you can get by\n"
                                                "3) Leave the city gates\n"))

                        if interaction == 1:
                            print("City Guard: Kidnapping you say? Haven't heard anything about that. ")
                            # ADD CLUE ABOUT OBSERVATION
                        elif interaction == 2:
                            if "City Pass" in player.inventory:
                                print("City Guard: Oh, you have a city pass. You may proceed. Stay safe!")
                                self.__guard_interacted = True
                            else:
                                print("City Guard: Hold! You can't enter without a city pass.")
                        elif interaction == 3:
                            print("City Guard: Safe travels, stranger.")
                            self.__guard_interacted = True
                else:
                    print("You already interacted with the city guard.")
            elif action == "2":
                self.explore_surroundings()
            elif action == "3":
                print("You look around to see if there is a way to get into the city.")

                distraction_option = input("1) Look for a distraction\n"
                                           "2) Return to the previous options\n")

                if distraction_option == "1":
                    print("While scanning the surroundings, you notice a group of barbarians nearby.")

                    bribe_option = input("The barbarians seem rowdy but open to negotiation.\n"
                                         "Perhaps they are willing to do something for a little bit of coin\n"
                                         "Do you want to approach them?\n"
                                         "1) Yes, approach the barbarians\n"
                                         "2) No, return to the previous options\n")

                    if bribe_option == "1":
                        if self.player.coins >= 25:
                            print("You approach the barbarians and offer them 25 coins to create a distraction.")
                            print("They gladly accept the offer and create a commotion, distracting the guards.")
                            print("With the distraction in place, you slip past the guards and enter the city.")
                            self.__guard_interacted = True
                            self.current_location = "City Streets"
                            self.player.coins -= 25
                        else:
                            print("You don't have enough coins to bribe the barbarians.")
                            print("You decide to explore other options.")
                    elif bribe_option == "2":
                        print("You decide not to approach the barbarians and look for alternative options.")
                    else:
                        print("Invalid option.")
                elif distraction_option == "2":
                    print("You decide to return to the previous options.")

        if self.current_location == "City Streets":
            print(f"You have entered the city! You are now in the {self.current_location}.")
            print("The hustle and bustle of the city's inhabitants surrounds you.")

    def explore_surroundings(self):
        print("You notice a dark alley at the back of the city walls")
        while True:
            exploration_result = input("1) Investigate the dark alley\n"
                                       "2) Examine the back of the city walls\n"
                                       "3) Return to the city gates\n")

            if exploration_result == "1" and not self.__dark_alley_investigated:
                print("You decide to investigate the dark alley.")
                print("As you enter the narrow alley, you hear a faint sound.")

                event_result = input("1) Follow the sound\n"
                                     "2) Go deeper into the alley\n"
                                     "3) Leave the alley\n")

                if event_result == "1":
                    print("You follow the sound and discover a hidden door.")
                    print("Behind the door, you find a group of hooded figures planning a secret meeting.")
                    print("They almost notice you, but you were able to slip away before they caught you.")

                    self.add_clue("secret meeting under city")
                    self.__dark_alley_investigated = True

                elif event_result == "2":
                    print("You decide to go deeper into the alley.")
                    print("After navigating through the narrow passages, you find yourself at the bottom of a well.")
                    print("You climb up and find yourself inside the city walls.")
                    self.current_location = "City Streets"
                    break

                elif event_result == "3":
                    print("You decide to leave the dark alley.")

                else:
                    print("Invalid option.")

            elif exploration_result == "1" and self.__dark_alley_investigated:
                print("You don't want to go back in there as the group of people might see you")

            elif exploration_result == "2":
                print("You examine the back of the city walls.")
                # Add puzzle logic or other events related to examining the city walls (to be implemented later)

            elif exploration_result == "3":
                print("You decide to return to the city gates.")
                break  # Exit the loop to go back to the initial exploration menu

            else:
                print("Invalid option.")

        if self.current_location == "City Streets":
            print(f"You have entered the city! You are now in the {self.current_location}.")
            print("The hustle and bustle of the city's inhabitants surrounds you.")


if __name__ == "__main__":
    player = Player("Player Name")
    player.coins = 25
    level2 = Level2(player)

    level2.outside_city()
