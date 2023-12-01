class Player:
    # Constructor method to initialize a new player with a name
    def __init__(self, name):
        self.name = name  # Player's name
        self.inventory = []  # List to store player's items
        self.main_clues = []  # List to store main clues collected by the player
        self.level_clues = []  # List to store level-specific clues
        self.coins = 0  # Initialize player's coin count
        print(f"Welcome {name}!\n")  # Greeting message to the player

    # Method to display all items in the player's inventory
    def show_inventory(self):
        print("The items in your inventory are:\n")
        for item in self.inventory:
            print(item + '\n')

    # Method to display all main clues collected by the player
    def show_main_clues(self):
        print("Main Clues are:\n")
        for main_clue in self.main_clues:
            print(main_clue + '\n')

    # Method to display all level-specific clues collected by the player
    def show_level_clues(self):
        print("Level Clues are:\n")
        for level_clue in self.level_clues:
            print(level_clue + '\n')
    
    # Method to add an item to the player's inventory
    def add_item(self, item):
        self.inventory.append(item)

    # Method to add a main clue to the player's collection
    def add_main_clue(self, main_clue):
        self.main_clues.append(main_clue)
    
    # Method to add a level-specific clue to the player's collection
    def add_level_clue(self, level_clue):
        self.level_clues.append(level_clue)
