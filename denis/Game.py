from Player import Player
from Levels import Level1
from Levels import Level2
from Levels import Level3
from Levels import Level4
from Levels import Level5
from Levels import Level6

class Game:
    def __init__(self):
        self.game_run = True  # Flag to keep track of the game state
        self.next_level = 0   # Index for the next level to be played

        # Prompting the user to enter a name for the player
        self.player_name = input("Welcome Adventurer!\nEnter a name please: \n")
        self.player = Player(self.player_name)  # Creating a new Player instance with the entered name

        # Initializing all levels.
        level1 = Level1(self.player)
        level2 = Level2(self.player)
        level3 = Level3(self.player)
        level4 = Level4(self.player)
        level5 = Level5(self.player)
        level6 = Level6(self.player)
        self.levels = [level1, level2, level3, level4, level5, level6]  # Storing the initialized levels in a list

    def game_running(self):
        # Method to check if the game is still running
        if self.game_run:
            return 1
        return 0

    def level_picker(self):
        # Looping through each level until all levels are completed
        while self.next_level < len(self.levels):
            # Starting the next level and then incrementing the level index
            self.levels[self.next_level].level_start()
            self.next_level += 1
        self.game_run = False  # Setting the game state to not running after completing all levels

# Creating an instance of the Game
game = Game()

# Checking if the game is running
if game.game_running():
    # If the game is running, start and progress through levels
    game.level_picker()
