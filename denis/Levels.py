from abc import ABC, abstractmethod
import time 

from Locations import LuminousLake
from Locations import WhisperingGrove
from Locations import CanopyWalkway
from Locations import EchoingCaverns

class Level(ABC):
    def __init__(self,player):
        self.player = player

    @abstractmethod
    def introduction(self):
        pass

    @abstractmethod
    def level_start(self):
        pass

class Level4(Level):
    def __init__(self, player):
        super().__init__(player)
        # Setting up the locations
        self.luminous_lake = LuminousLake(self.player)
        self.whispering_grove = WhisperingGrove(self.player) 
        self.canopy_walkway = CanopyWalkway(self.player)
        self.echoing_caverns = EchoingCaverns(self.player)
        self.locations = [self.luminous_lake, self.whispering_grove,
        self.canopy_walkway, self.echoing_caverns] 
        self.current_pos = 0
    def introduction(self):
        print("You find yourself in a luminous glade, the air filled with spores that glimmer" 
        " like tiny stars.\n")
        time.sleep(1)
        print("Gigantic mushrooms tower over you, their caps glowing softly in an array of colors.\n")
        time.sleep(1)
        print("The path behind you fades into the forest, hinting at the way back.\n")
        time.sleep(1)
        print("A gentle, misty breeze whispers through the trees, carrying distant, melodic sounds.\n")
        time.sleep(1)
        print("The path ahead winds deeper into the forest, where the mushrooms grow denser and" 
        " the air is thick with mystery.\n")

    def level_start(self):
        self.introduction()

        while True:
            print("---Type anything to continue---\n")
            continue_game = input()
            print("-------------------------------------------------------")
            for index,location in enumerate(self.locations):
                print(f"{index + 1}) Would you like to go to {self.locations[index].name}\n")

            print(f"{(len(self.locations) + 1)}) to view your Inventory\n")
            print(f"{(len(self.locations) + 2)}) to view your Clues\n")
            print("-------------------------------------------------------")

            # This was from Josha. He saved me from losing my sanity over this shit. 
            while True:
                try:
                    choice = int(input("").lower())
                    if choice == (len(self.locations) + 1):
                        self.player.show_inventory()
                    if choice == (len(self.locations) + 2):
                        self.player.show_main_clues()
                        self.player.show_level_clues()
                    break
                except Exception:
                    print("Invalid Input!")
            for index,location in enumerate(self.locations):
                if choice == (index + 1):
                    self.locations[index].location_scene()