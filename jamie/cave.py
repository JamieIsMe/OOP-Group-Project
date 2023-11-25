from sean.locationClass import Location

class Cave(Location):
    def __init__(self):
        super().__init__("cave", ["entrance", "walkway"],
                         ["John Pork", "Joe Bibiden", "Jo Mama"], ["Peter Did It"])
        self.current_location = "entrance"
        self.visited_sublocations = []
        self.location_states = [False]*1

    def visited(self):
        self.visited_sublocations.append(self.current_location)

    def entrance(self):
        if self.current_location not in self.visited_sublocations:
            print("As you cautiously step into the dimly lit cave, two things stand out to you, iron bars with a door"
                  "blocking further access into the cave and drawings on the cave walls")
            self.visited()
        else:
            print("As you enter back in to the cave entrance, you take another look at the iron bars "
                  "with a door and the drawings")
        while self.current_location == "entrance":
            if not self.location_states[0]:
                action = input(f"What will you do?\n1) Turn back around\n2) Go to the iron door\n3) Check the walls\n")
                if action == "1":
                    print("As you attempt to make your way back out of the cave, you trip on a rock, somehow "
                          "causing the entrance to cave in")
                    self.location_states[0] = True
                elif action == "2":
                    # IF PLAYER HAS NO KEY
                    print("You approach the door and see that it's locked, however you don't have a key to unlock it")
                    # IF PLAYER HAS KEY
                    print("You approach the door and see that it's locked. You use your key and manage to unlock the "
                          "door and pass through")
                elif action == "3":
                    print("wow this wall is made of wall")
            else:
                action = input("What will you do?\n1) Go to the iron door\n2) Check the walls\n")
                if action == "1":
                    print("its made of iron, what did you expect?")
                elif action == "2":
                    print("wow this wall is made of wall")
            print()

    def walkway(self):
        self.current_location = "walkway"
        if self.current_location not in self.visited_sublocations:
            print("")
            self.visited()
        else:
            print("")

if __name__ == "__main__":
    cave = Cave()
    cave.entrance()
