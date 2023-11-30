from denis import Player

class Game:
    def __init__(self):
        self.game_run = True
        self.next_level = 1

        self.player_name = input("Welcome!\nEnter a name please: \n")
        self.player = Player(self.player_name)

        level1 = Level1(self.player)
        level2 = Level2(self.player)
        level3 = Level3(self.player)
        level4 = Level4(self.player)
        level5 = Level5(self.player)
        level6 = Level6(self.player)
        self.levels = [level1, level2, level3, level4, level5, level6]

    def game_running(self):
        if self.game_run:
            return 1
        return 0

    def level_picker(self):
        self.levels[self.next_level].level_start()
        self.next_level += 1


game = Game()

if game.game_running():
    game.level_picker()
