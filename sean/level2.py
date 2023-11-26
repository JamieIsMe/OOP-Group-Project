from cian.chartacters import Character
from sean.locationClass import Location


class Level2(Location):
    def __init__(self, score, coins):
        super().__init__("City", "Outside City Walls", [], [])
        self.current_location = "entrance to the city"
        self.score = score
        self.coins = coins
        self.visited_locations = []
        self.city_guard = NPC("City Guard",
                              "Halt! What business do you have here, stranger?",
                              "Overheard some shady characters talking near the city gates.",
                              "City Map")

        # Boolean variable set for no double interaction with the city guard
        self.__guard_interacted = False

    def outside_city(self):
        print(f"{self.current_location.capitalize()} - A cold night outside the city walls.\n"
              f"You see the silhouette of the towering city gates ahead of you, guarded by vigilant city guards.")

        while self.current_location == "entrance to the city":
            action = input("\nWhat will you do?\n"
                           "1) Approach the city gates\n"
                           "2) Explore the surroundings\n"
                           "3) Wait for something to happen\n")

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
                            if "City Pass" in player.items:
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
                print(
                    "You decide to explore the surroundings, looking for any interesting clues or points of interest.")
                exploration_result = self.explore_surroundings()
                if exploration_result == "secret_entrance":
                    print("You discover a secret entrance at the back of the city walls. "
                          "You quietly sneak into the city.")
                    self.current_location = "City Streets"
                    print(f"You are now in the {self.current_location}.")
                    print("The hustle and bustle of the city streets surround you.")
                elif exploration_result == "nothing_special":
                    print("You don't find anything particularly interesting.")
            elif action == "3":
                print("You decide to wait for something to happen.")
                # Add waiting logic here

    def explore_surroundings(self):
        # Simulate the player exploring the surroundings
        exploration_result = input("You notice a dark alley and the back of the city walls.\n"
                                   "1) Investigate the dark alley\n"
                                   "2) Examine the back of the city walls\n"
                                   "3) Return to the city gates\n")

        if exploration_result == "1":
            print("You find a stray cat in the dark alley.")
            # Add possible actions when investigating the dark alley
        elif exploration_result == "2":
            return "secret_entrance"
        elif exploration_result == "3":
            return "return_to_gates"
        else:
            return "nothing_special"

        # Once the player has interacted with the city guard, update the location
        self.current_location = "City Streets"
        print(f"You have entered the city! You are now in the {self.current_location}.")
        print("The hustle and bustle of the city streets surround you.")


if __name__ == "__main__":
    level2 = Level2(1, 50)
    player = Character("Player Name", "Greetings, adventurer!", [], [])

    level2.outside_city()
