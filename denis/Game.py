from Player import Player
from Level import Level4 

class Game:
    def __init__(self):
        self.game_run = True  # Flag to keep track of the game state
        self.next_level = 1   # Index for the next level to be played

        # Prompting the user to enter a name for the player
        self.player_name = input("Welcome Adventurer!\nEnter a name please: \n")
        self.player = Player(self.player_name)  # Creating a new Player instance with the entered name

        # Initializing the levels. Note: Only Level1 and Level4 are initialized. Others are commented out.
        level1 = Level1(self.player)
        # level2 = Level2(self.player)
        # level3 = Level3(self.player)
        level4 = Level4(self.player)
        # level5 = Level5(self.player)
        # level6 = Level6(self.player)
        self.levels = [level1, level4]  # Storing the initialized levels in a list
    def game_running(self):
        # Method to check if the game is still running
        if self.game_run:
            return 1
        return 0

    def level_picker(self):
        # Method to start the next level and then increment the level index
        self.levels[self.next_level].level_start()
        self.next_level += 1

# Creating an instance of the Game
game = Game()

# Here, the game checks if it is still running.
if game.game_running():
    # If the game is running, it then picks and starts the next level using the level_picker method
    game.level_picker()
