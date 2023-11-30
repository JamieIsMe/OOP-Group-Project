from sean.locationClass import Location
from cian.characters import NPC
from denis.Player import Player
import time


class Cave(Location):
    def __init__(self):
        super().__init__("cave", ["entrance", "walkway", "cursed_hallway", "deep_cursed_hallway"],
                         ["Man In Cell", "Joe Bibiden", "Jo Mama"], ["Peter Did It"])
        self.current_location = "entrance"
        self.location_states = [False] * 3
        self.user = Player("Jamie")
        # TEMP SCORE VARIABLE UNTIL PLAYER CLASS FINISHED
        self.cell_man = NPC("Man In Cell", "If you open my cell, I will help you get through that door", "", "")
        self.cult_leader = NPC("Cult Leader", ["So you have finally arrived." , "We will revive the witch slayer so "
                                                                               "that she may save us all"], "", "")

    def entrance(self):
        self.current_location = self.sublocation[0]
        if self.current_location not in self.visited_sublocations:
            print("As you cautiously step into the dimly lit cave, two things stand out to you, iron bars with a door"
                  "blocking further access into the cave and drawings on the cave walls")
            self.visited(self.current_location)
        else:
            print("As you enter back in to the cave entrance, you take another look at the iron bars "
                  "with a door and the drawings")
        while self.current_location == "entrance":
            if not self.location_states[0]:
                action = input(f"What will you do?\n1) Turn back around\n2) Go to the iron door\n3) Check the walls\n")
                if action == "1":
                    print("As you attempt to make your way back out of the cave, you trip on a rock, somehow "
                          "causing the entrance to cave in\nUnder the rock you tripped on, you find a key and pick it "
                          "up")
                    self.user.add_item("key")
                    self.location_states[0] = True
                elif action == "2":
                    if "key" not in self.user.inventory:
                        print(
                            "You approach the door and see that it's locked, however you don't have a key to unlock it")
                    elif "key" in self.user.inventory:
                        print(
                            "You approach the door and see that it's locked. You use your key and manage to unlock the "
                            "door and pass through\n")
                        self.walkway()
                elif action == "3":
                    if " - 5 people, The 2nd and 4th are kneeling down" not in self.user.clues:
                        self.user.add_clue(" - 5 people, The 2nd and 4th are kneeling down")
                    print("Looking closer at the drawing, you see 5 people in robes surrounding a statue. The second "
                          "and fourth are kneeling down")
            else:
                action = input("What will you do?\n1) Go to the iron door\n2) Check the walls\n")
                if action == "1":
                    if "key" not in self.user.inventory:
                        print(
                            "You approach the door and see that it's locked, however you don't have a key to unlock it")
                    elif "key" in self.user.inventory:
                        print(
                            "You approach the door and see that it's locked. You use your key and manage to unlock the "
                            "door and pass through\n")
                        self.walkway()
                elif action == "2":
                    if " - 5 people, The 2nd and 4th are kneeling down" not in self.user.clues:
                        self.user.add_clue(" - 5 people, The 2nd and 4th are kneeling down")
                    print("Looking closer at the drawing, you see 5 people in robes surrounding a statue. The second "
                          "and fourth are kneeling down")
            print()

    def walkway(self):
        state = ["down"] * 5
        self.current_location = self.sublocation[1]
        if self.current_location not in self.visited_sublocations:
            print("You find yourself in a new room. You can see that there are 5 cells along the wall and a door at "
                  "the end of the room")
            self.visited(self.current_location)
        else:
            print("")
        while self.current_location == "walkway":
            action = input("What Will You Do?\n1) Look at the cells\n2) Go to the door\n3) Turn back around\n")
            if action == "1":
                Talking = True
                if not self.location_states[1]:
                    print("when you look at the cells you notice that someone is sitting inside one of the cells. "
                          "Before you can say anything, they speak.")
                    print(self.cell_man.say_dialogue(self.cell_man.dialogue))
                elif self.location_states[1]:
                    print("You return to the cell to see that the man has disappeared but he left a note on the "
                          "floor\nYou pick it up and see that its says 5481")
                    if " - Note that says 5481" not in self.user.clues:
                        self.user.add_clue(" - Note that says 5481")
                else:
                    print("You return back to the person in the cell")
                while Talking:
                    if not self.location_states[1]:
                        action = input(
                            "What will you do?\n1) Ask who they are\n2) Ask how to open their cell\n3) Go back\n")
                        if action == "1":
                            print(
                                self.cell_man.perform_action(": I am a member of the cult, I had doubts about what we "
                                                             "were doing so the rest of them locked me in here"))
                        elif action == "2":
                            print(self.cell_man.perform_action(": There are levers that you will have to flip, i don't "
                                                               "know which ones you have to flip"))
                        elif action == "3":
                            print("You go back to the centre of the room")
                            Talking = False
                    else:
                        Talking = False
            elif action == "2":
                print("You walk up to the door and attempt to open it but it wont budge, beside the door door you "
                      "notice a keypad and 5 levers")
                door_interaction = True
                while door_interaction:
                    action = input("What will you do?\n1) Look at the keypad\n2) Look at the levers\n3) Go back\n")
                    if action == "1":
                        keypad = True
                        while keypad:
                            action = input(
                                "The keypad needs a 4 digit code.\n1) Try enter a code\n2) View Clues\n3) Go Back\n")
                            if action == "1":
                                code = input("Please enter a code: ")
                                if code == "5481":
                                    print("You hear a click as the door swings open.\nYou feel an eerie chill that "
                                          "envelops you and pulls you in\nThe door slams shut behind you\n")
                                    self.cursed_hallway()
                            elif action == "2":
                                print("You take a look at your clues: ", end="")
                                print(*self.user.clues)
                            elif action == "3":
                                print("You move back to the center of the room\n")
                                keypad = False

                    elif action == "2":
                        if not self.location_states[1]:
                            lever_interaction = True
                            print("You look at the levers and see that all five are flipped up")
                            while lever_interaction:
                                action = input(
                                    f"What will you do?\n1) Flip lever 1 {state[0]}\n2) Flip lever 2 {state[1]}\n"
                                    f"3) Flip lever 3 {state[2]}\n4) Flip lever 4 {state[3]}\n"
                                    f"5) Flip lever 5 {state[4]}\n6) View Clues\n7) Go back\n")
                                if action == "1":
                                    state[0] = "up" if state[0] == "down" else "down"
                                    print(f"You flipped lever 1")
                                elif action == "2":
                                    state[1] = "up" if state[1] == "down" else "down"
                                    print(f"You flipped lever 2")
                                elif action == "3":
                                    state[2] = "up" if state[2] == "down" else "down"
                                    print(f"You flipped lever 3")
                                elif action == "4":
                                    state[3] = "up" if state[3] == "down" else "down"
                                    print(f"You flipped lever 4")
                                elif action == "5":
                                    state[4] = "up" if state[4] == "down" else "down"
                                    print(f"You flipped lever 5")
                                elif action == "6":
                                    print("You take a look at your clues: ", end="")
                                    print(*self.user.clues)
                                elif action == "7":
                                    lever_interaction = False
                                if state[0] and state[2] and state[4] == "down":
                                    if state[1] and state[3] == "up":
                                        lever_interaction = False
                                        self.location_states[1] = True
                                        print("You hear a click and a door open behind "
                                              "you. The levers are now stiff and you cant "
                                              "move them")
                        else:
                            print("The levers are stuck in place, you cant move them "
                                  "anymore")
                    elif action == "3":
                        door_interaction = False
            elif action == "3":
                print("You turn around and head back through the door you came from")
                self.entrance()

    def cursed_hallway(self):
        self.current_location = self.sublocation[2]
        time.sleep(1)
        print("As you take a look ahead, you notice that the passage stretchs endlessly before "
              "you, the vanishing point obscured by an otherworldly haze\n")
        time.sleep(3)
        print("The walls surrounding you are adorned with an ancient script that you are unable to "
              "comprehend.\nYou take your first steps down the passage\n")
        time.sleep(3)
        print(
            "You keep walking the end still seems to be nowhere in sight.The air grows heavier with each passing step.\n")
        time.sleep(3)
        print(
            "Suddenly you feel a strong pulsating wave from ahead of you. You stop dead in your tracks, and thats when you notice it.\n")
        time.sleep(2)
        for i in "YOU ARE BEING WATCHED":
            print('\033[91m' + i + '\033[0m', end="")
            time.sleep(0.5)
        time.sleep(1)
        while self.current_location == "cursed_hallway":
            choice = input("\nWhat will you do?\n1) Continue on forward\n2) Run away\n")
            if choice == "1":
                self.deep_cursed_hallway()
            elif choice == "2":
                self.ran_away()

    def deep_cursed_hallway(self):
        self.current_location = self.sublocation[3]
        print("You steel yourself for what's to come and take another step forward")
        time.sleep(2)
        print("\nWith each passing step you hear a noise get louder and louder, eventually forming words")
        time.sleep(3)
        print('\033[91m' + '\033[1m' + "Sanguis bibimus" + "\nCorpus edibus" + '\033[0m')
        time.sleep(2)
        print("\nYou are finally able to see an end to the passage, a small door")
        time.sleep(2)
        print("\nYou find yourself standing in front of the door, all previous sounds have disappeared and its now "
              "deathly quiet.\nIt seems your presense is known")
        time.sleep(2)
        while True:
            action = input("Its too late to turn back now\nWhat will you do?\n1) Enter the door\n")
            if action == "1":
                break
        print("You burst through the door and are met face to face with 5 cult members surrounding a corpse")
        print(self.cult_leader.say_dialogue(self.cult_leader.dialogue[0]))
        while self.current_location == "deep_cursed_hallway":
            print("\nWhat will you do?\n1) Ask what their plan is\n2) Attempt to stop them\n3) Let them preform their "
                  "plan")
            talking = True
            while talking:
                action = input("\nWhat will you do?\n1) Ask what their plan is\n2) Attempt to stop them\n3) Let them "
                               "preform their plan")
                if action == "1":
                    print(self.cult_leader.say_dialogue(self.cult_leader.dialogue[1]))
                elif action == "2":
                    pass
                elif action == "3":
                    print("\nYou decided to let the cultists preform their plan")

    def ran_away(self):
        # Finish this ending
        print("You can hear a booming laughter coming from behind you as you run away")


if __name__ == "__main__":
    cave = Cave()
    # cave.entrance()
    cave.cursed_hallway()
