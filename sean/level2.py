from cian.characters import Character, NPC
from sean.locationClass import Location

# Change the explore_surroundings to include options for examining back walls and other options


class PlayerCharacter(Character):
    def __init__(self, name, dialogue, clue, item):
        super().__init__(name, dialogue, clue, item)

    def perform_action(self, action):
        # Implement the desired behavior for the player's character
        pass


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
        # Boolean variable to track whether the dark alley has been investigated
        self.__dark_alley_investigated = False
        # Boolean variable to track whether the event in the dark alley has occurred
        self.__event_occurred = False

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
        while True:
            if not self.__dark_alley_investigated:
                exploration_result = input("You notice a dark alley at the back of the city walls.\n"
                                           "1) Investigate the dark alley\n"
                                           "2) Examine the back of the city walls\n"
                                           "3) Return to the city gates\n")

                if exploration_result == "1":
                    print("You decide to investigate the dark alley.")
                    print("As you enter the narrow alley, you hear a faint sound.")

                    # Simulate an event in the dark alley
                    event_result = input("1) Follow the sound\n"
                                         "2) Continue exploring the alley\n"
                                         "3) Leave the alley\n")

                    if event_result == "1":
                        print("You follow the sound and discover a hidden door.")
                        print("Behind the door, you find a group of people planning a secret meeting.")
                        print("They almost notice you, but you were able to slip away before they caught you.")

                        self.add_clue("secret meeting under city")
                    elif event_result == "2":
                        print("You continue exploring the dark alley and see some light coming from above."
                              "You can hear the commotion of the city above you and realize you are at the bottom of a "
                              "well."
                              "You climb up and find yourself inside the city walls")

                    elif event_result == "3":
                        print("You decide to leave the dark alley.")
                    else:
                        print("Invalid option.")

                    self.__dark_alley_investigated = True  # Set the flag to True for subsequent interactions

            else:
                exploration_result = input("You have already investigated the dark alley.\n"
                                           "1) Examine the back of the city walls\n"
                                           "2) Return to the city gates\n")

                if exploration_result == "1":
                    print("You continue exploring the dark alley and see some light coming from above.")
                    print("You hear the commotion of the city above you and realize you are at the bottom of a well.")
                    print("You climb up and find yourself inside the city walls")
                    break  # Exit the loop to proceed with entering the city

                elif exploration_result == "2":
                    print("You decide to leave the dark alley.")

            # Break the loop if the player has entered the city
            if self.current_location == "City Streets":
                break

            # Once the player has interacted with the city guard or explored the surroundings,
            # update the location if necessary.
        print(f"You have entered the city! You are now in the {self.current_location}.")
        print("The hustle and bustle of the city's inhabitants surround you.")


if __name__ == "__main__":
    level2 = Level2(1, 50)
    player = PlayerCharacter("Player Name", "Greetings, adventurer!", [], [])

    level2.outside_city()
