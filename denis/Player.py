class Player:

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.clues = []
        self.coins = 0
        print(f"Welcome {name}!\n")

    def show_inventory(self):
        print("The items in your inventory are:\n")
        for item in self.inventory:
            print(item + '\n')

    def show_clues(self):
        print("Your clues are:\n")
        for clue in self.clues:
            print(clue + '\n')

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def add_clue(self, clue):
        self.clues.append(clue)
