class Location:
    def __init__(self, location, sublocation, location_npcs, clues, visited):
        self.location = location
        self.sublocation = sublocation
        self.location_NPCs = location_npcs
        self.__clues = clues
        self.visited_sublocations = []

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

    def visited(self, location):
        self.visited_sublocations.append(location)

    def view_visited_locations(self):
        return f"You have visited {self.visited_sublocations}"

    def whoishere(self):
        return self.location_NPCs
