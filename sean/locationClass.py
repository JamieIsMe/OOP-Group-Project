class Location:
    def __init__(self, location, sublocation):
        self.location = location
        self.sublocation = []
        self.location_NPCs = []
        self.__clues = []

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clues(self):
        return self.__clues

    def location_npcs(self, npc):
        self.location_NPCs.append(npc)

    def general_location(self):
        return f"You are in {self.location}"

    def specific_location(self):
        return self.sublocation

    def whoishere(self):
        return self.location_NPCs
