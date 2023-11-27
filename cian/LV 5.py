from sean.locationClass import Location
from cian.characters import NPC
from cian.Dice_minigame import dice_game


class Camp(Location):
    def __init__(self, score, coins):
        super().__init__("camp", ["outer_camp", "main_camp", "hut_1", "big_hut", "side_main_camp"],
                         ["Goblin trio", "Dice Goblin", "Goblin Elder"],
                         ["Goblin elder is in the big hut", "Dicy's clue"])
        self.current_location = "outer_camp"
        self.visited_sublocations = []
        self.location_states = [False] * 3
        self.score = score
        self.coins = coins
        self.goblin_trio = NPC("Goblin trio", "", "", "")
        self.dice_goblin = NPC("Dicy", "", "", "")

    def visited(self):
        self.visited_sublocations.append(self.current_location)

    def outer_camp(self):
        self.current_location = "outer_camp"
        if self.current_location not in self.visited_sublocations:
            print("Emerging from the dense forest, you spot a small goblin camp at the foot of towering cliffs."
                  "Ramshackle huts, constructed from salvaged materials, form a chaotic maze in the shadows."
                  "Flickering bonfires illuminate the primitive dwellings. "
                  "You spot 3 shadows dart into the nearest hut")
            self.visited()
        else:
            print("You walk back out of the camp and look back at it, Not much has changed\n")

        while self.current_location == "outer_camp":

            choice = input(f"What will you do?\n1) Investigate the first Hut\n2) Walk deeper into the camp\n"
                           "3) Keep observing the camp from outside\n")
            # to 1st hut
            if choice == "1":
                print("As you enter the camp you come to the realisation that you cant see any sign of the residents.")
                self.hut_1()

            # to main camp
            elif choice == "2":
                print("You walk past the first hut and deeper into the town")
                self.main_camp()

            # stay where they are
            elif choice == "3":
                self.outer_camp()

    def hut_1(self):
        self.current_location = "hut_1"
        if self.current_location not in self.visited_sublocations:
            print("You come up to the door of the first hut where you saw the 3 shadows enter\n")
            self.visited()
        else:
            print("As you approach the hut you see that the door is open and nobody is inside. "
                  "The goblin trio has left\n"
                  "You walk deeper into the camp\n")
            self.main_camp()

        while self.current_location == "hut_1":
            choice = input("\nWhat will you do?\n1) Knock on the door\n2) Try to open it\n"
                           "3) Walk deeper into the camp\n")
            interacting = True
            if choice == "1":
                print("You here a high pitched voice from the other side\n'Nobody is home'!\n")
                interacting = True
            elif choice == "2":
                print("You try to open the door by force with little success")
                print(self.goblin_trio.say_dialogue(":'You are not getting we have the door barred'!"
                                                    "The voices on the other side shout\n"))
                interacting = True
            elif choice == "3":
                self.main_camp()

            while interacting:
                choice = input("What will you do?\n1) Say that you just want to talk and you mean no harm\n"
                               "2) Try to open the door\n3) Leave and go further into the town\n")

                if choice == "1":
                    print("The door opens slightly and you see 3 Goblins peer through the crack nervously\n")
                    print(self.goblin_trio.say_dialogue(":You here voices in unison say:\n'What do you want'?"))

                    choice = input("How do you respond?\n1) 'I just wanted to see if you have any information on"
                                   "some missing people'\n2)'Wrong hut sorry'. Leave and go further into the town\n")
                    if choice == "1":
                        print("The Goblin trio open the door further and you see 3 identical goblins."
                              "The only difference is their eye colour\n")

                        print(("First Goblin: 'We heard the elder talk about that\n"
                               "Second Goblin: 'We dont know nothing'\n"
                               "Third Goblin: 'The elder should be in the big hut'\n"))

                        choice = input("Where will you go next?\n1) Go back to the outside of the camp.\n"
                                       "2) Go deeper into the village to find the elder.\n")

                        if choice == "1":
                            interacting = False
                            self.outer_camp()
                        elif choice == "2":
                            interacting = False
                            self.main_camp()

                    elif choice == "2":
                        interacting = False
                        self.main_camp()

                elif choice == "2":
                    print("You try to open the door by force with little success")
                    print(self.goblin_trio.say_dialogue(":'You are not getting we have the door barred'!"
                                                        "The voices on the other side shout\n"))
                elif choice == "3":
                    print("You go back to the centre of the room")
                    interacting = False
                    self.main_camp()

    def main_camp(self):
        self.current_location = "main_camp"
        if self.current_location not in self.visited_sublocations:
            print("You arrive in the center of the camp.\nFrom here you can see the entire camp."
                  "\n\nSome points of interest include:\n"
                  "1. The First Hut\n2. The Big Hut with 2 angry looking goblins guarding the entrance.\n"
                  "3. A Goblin in a long trench coat and large hat "
                  "sitting on the ground with a set of dice in front of him.\n")
            self.visited()

        choice = input("\nWhere will you go?\n"
                       "1) Back to the First Hut\n"
                       "2) To the Big Hut\n"
                       "3) Over to the Suspicious Goblin\n"
                       "4) Leave Camp\n")

        if choice == "1":
            self.hut_1()
        elif choice == "2":
            self.big_hut()
        elif choice == "3":
            self.side_main_camp()
        elif choice == "4":
            self.outer_camp()

    def big_hut(self):
        print("\nno\n")
        self.main_camp()

    def side_main_camp(self, coins=100):
        self.current_location = "sus_goblin"
        if self.current_location not in self.visited_sublocations:
            print("You walk over to the Shady Goblin\n")
            print("Shady Goblin: Welcome friend!\nIf im not mistaken you're new around here.\nThe names Dicy")
            self.visited()
        if coins == 100:
            print(self.dice_goblin.say_dialogue("Well friend you seem mighty well off "
                                                "how abouts i give you some information "
                                                "as a fellow benefactor of life"))
            # add clue
            print("Now dont go spreading this info around")

        print(self.dice_goblin.say_dialogue("Fancy a game of dice friend"))
        minigame_played = False
        if not minigame_played:
            choice = input("1) Yes\n2) No\n")
            if choice == "1":
                dice_game()
            elif choice == "2":
                print("You decline and return to the center of camp")
                self.main_camp()
        else:
            print(self.dice_goblin.say_dialogue("How about another round"))
            choice = input("1) Yes\n2) No\n")
            if choice == "1":
                dice_game()
            elif choice == "2":
                print("You decline and return to the center of camp")
                self.main_camp()


if __name__ == "__main__":
    camp = Camp(0, 0)
    camp.outer_camp()
