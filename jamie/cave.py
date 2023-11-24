from sean.locationClass import Location


class Cave(Location):
    def __init__(self):
        super().__init__("cave", ["cavern", "entrance"],
                         ["John Pork", "Joe Bibiden", "Jo Mama"], ["Peter Did It"])
        self.current_location = "entrance"

    def entrance(self):
        print("As you cautiously step into the dimly lit cave, two things stand out to you, iron bars with a dw"
              "blocking further access into the cave and drawings on the cave walls")
        while self.current_location == "entrance":

            # EXAMPLE: LIST OF ACTIONS
            action = input("What Will You Do?\n1) Turn back around\n2) Go to the iron door\n3) Check the walls\n")
            if action == "1":
                print("As you attempt to make your way back out of the cave, you trip on a rock, somehow causing the "
                      "entrance to cave in")
            elif action == "2":
                print("its made of iron, what did you expect?")
            elif action == "3":
                print("wow this wall is made of wall")

if __name__ == "__main__":
    cave = Cave()
    cave.entrance()
