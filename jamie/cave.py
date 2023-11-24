from sean.locationClass import Location


class Cave(Location):
    def __init__(self):
        super().__init__("cave", ["cavern", "entrance"],
                         ["John Pork", "Joe Bibiden", "Jo Mama"], ["Peter Did It"])
        self.current_location = "entrance"

    def entrance(self):
        print("As you cautiously step into the dimly lit cave, two things stand out to you, iron bars with a door "
              "blocking further access into the cave and drawings on the cave walls")
        while self.current_location == "entrance":
            # Should Use List Of Possible Actions And Input With Numbers? or vague Ask What The user wants to do and
            # let them type in keywords like "door" "bars" or "wall" "painting"
            self.current_location = "cavern"


if __name__ == "__main__":
    cave = Cave()
    cave.entrance()
