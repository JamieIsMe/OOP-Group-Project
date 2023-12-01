from abc import ABC, abstractmethod
from Character import NPC
import time 
import random 

class Location(ABC):  # Creating an abstract base class named 'Location'
    def __init__(self, player):  # Constructor method for initializing a new Location instance
        self.player = player  # Assigning a player object to the Location instance
        self.name = None  # Initializing the 'name' attribute to None (to be set in subclasses)
        self.level = None  # Initializing the 'level' attribute to None (to be set in subclasses)

    def check_item(self, key_item):  # Method to check for a specific item in the player's inventory
        for item in (self.player.inventory):  # Iterating through each item in the player's inventory
            if item == key_item:  # Checking if the current item matches the key_item
                self.player.inventory.remove(item)  # Removing the item from the inventory
                return 1  # Returning 1 to indicate the item was found and removed
        return 0  # Returning 0 if the item is not found in the inventory
    
    @abstractmethod  
    # Acts as the main method. Everything in the location happens here. 
    def location_scene(self): 
        pass  

class LuminousLake(Location):
    def __init__(self,player):
        self.player = player 
        self.name = "The Luminous Lake"
        self.item_pickups = ["Luminous Plank", "Ancient Paper"]        
        self.item_pickup = [False,False]                          
        self.next_item = 0                  
    def scene_lake(self):
        self.next_item = 0 # Reset the pointer to the item back to 0 
        print("A serene lake lies hidden among the giant mushrooms. Its waters are said to reflect hidden truths.\n")
        time.sleep(1)
        investigate = input("Would you like to check the Serene Lake? 'y' for yes:\n").lower()
        if investigate == 'y':
            if self.item_pickup[self.next_item]:
                print(f"You already found \"{self.item_pickups[self.next_item]}\"\n")
            else:
                self.player.add_item(self.item_pickups[self.next_item])
                print(f"You found a \"{self.item_pickups[self.next_item]}\" at surface of the Serene Lake!\n")
                self.item_pickup[self.next_item] = True
        else:
            print("As you bypass the Serene Lake, its tranquil waters glistening softly in the muted light," 
            " you can't help but wonder what secrets and reflections it might have revealed.\n")

    def scene_fallen_leaves(self):
        print("As you turn away from the Luminous Lake, a glint among the underbrush catches your eye." 
        " Curiosity piqued, you approach and find a piece of ancient, weathered paper partially buried under a layer of fallen leaves.\n")
        time.sleep(1)

        investigate = input("Press 'y' to investigate further.\n")

        if investigate == 'y':
            if self.item_pickup[self.next_item]:

                print(f"You already found \"{self.item_pickups[self.next_item]}\"\n")
            else:
                self.player.add_item(self.item_pickups[self.next_item])
                print(f"You found a \"{self.item_pickups[self.next_item]}\" under a layer of fallen leaves!\n")
                self.item_pickup[self.next_item] = True # We set the flag of the item we picked up.
            time.sleep(1) 
        else:
            print("As you hesitate, a gust of wind stirs the leaves, briefly obscuring the ancient paper from view." 
            " You decide to leave it undisturbed, its secrets remaining a part of the forest's untold history.\n")
            time.sleep(1)
        print("With one last glance at the serene waters of the Luminous Lake," 
        "reflecting the soft glow of the mushroom forest in its depths.\n")
        time.sleep(1)

    def location_scene(self):
        # Scene 1
        self.scene_lake()
        self.next_item += 1 # Point to the next item we want to reward 
        time.sleep(1)
        # Scene 2
        self.scene_fallen_leaves()

class WhisperingGrove(Location):
    def __init__(self,player):
        self.player = player 
        self.name = "The Whispering Grove"
        self.item_pickups = ["Silver Key"]   
        self.item_pickup = [False]                      
        self.next_item = 0  
        self.old_man = NPC("Old Man",None,"Seek the paper where still waters mirror the forest's canopy," 
        "hidden not in plain sight but where shadows mingle with the earth's whispers.\n",None)
        self.old_man_dialog = ["Ah, traveler! I am in dire need of assistance.",
        "I've lost an ancient paper," 
        "one of great importance to me and the secrets of this forest",
        "It contains knowledge passed down through generations.",
        "If you find it and bring it to me," 
        "I will gladly show you the way to a hidden path leading out of this forest."]
        self.seen_clue = 0
    
    def found_key(self):
        print("As you pass the spot where the old man once stood, your eye catches a glint on the forest" 
        "floor. There, nestled among the fallen leaves, lies a silver key, seemingly dropped by the old man."
        " \n")
        time.sleep(1)
        investigate = input("Press 'y' to investigate further.\n")
        if investigate == 'y':
            if self.item_pickup[self.next_item]:
                print(f"You already found \"{self.item_pickups[self.next_item]}\"\n")
            else:
                self.player.add_item(self.item_pickups[self.next_item])
                print(f"You found a \"{self.item_pickups[self.next_item]}\" on the mythstic forest dirt!\n")
                self.item_pickup[self.next_item] = True # We set the flag of the item we picked up.

    def scene_oldman(self):
        print("As you step into the Whispering Grove, the air seems to hum with a quiet energy.\n")
        time.sleep(1)
        print("The mushrooms here are tall and slender, their caps casting dappled shadows on the ground.\n")
        time.sleep(1)
        if self.old_man._interacted:
            print("As you make your way back to the spot where the old man once stood, a sense of quietude greets you.\n")
            time.sleep(1)
            print("Where there was once the presence of age-old wisdom and the subtle weight of ancient eyes," 
            "there is now only the gentle sway of the forest.\n")
            self.found_key()
            time.sleep(1)
            return 1
        else:
            print("In the midst of this serene setting, you notice an old man,"
            " his eyes reflecting wisdom and a touch of sadness. He seems to be searching for something desperately.\n")
            time.sleep(1)
            for dialog in self.old_man_dialog:
                print(self.old_man.say_dialogue(dialog) + '\n')
                time.sleep(1)
            while True:
                print("'c' to ask for a \"clue\"\n")
                print("'h' to hand the \"Ancient Paper\"\n")
                print("'b' to go back to \"Forest Path\"\n")

                hand_item = input()
                if hand_item == 'c':
                    if self.seen_clue:
                        print("You have already seen this clue!\n")
                    else:
                        self.player.add_level_clue(self.old_man.show_clue())
                        print(self.old_man.show_clue())
                        self.seen_clue = 1
                if hand_item == 'h':
                    if self.check_item("Ancient Paper"):
                        self.old_man._interacted = True 
                        print("Bless your heart! This paper is the key to understanding"
                        "many mysteries of these woods.\n")
                        time.sleep(1)
                        print("As promised, follow the northern trail from here," 
                        "and you'll find a hidden passage veiled by ivy.\n")
                        time.sleep(1)
                        print("It leads to new realms of this forest." 
                        "May your journey be filled with enlightenment and wonder.\n")
                        time.sleep(1)
                        print("As you hand the ancient paper to the old man, he smiles warmly,"
                        "his eyes reflecting a deep gratitude." 
                        "With a wave of his hand, he points you towards"
                        "a barely noticeable path shrouded in the mist.\n")
                        time.sleep(1)
                        self.found_key()
                        time.sleep(1)
                        break
                    else:
                        print("It seems you do not possess what you seek to offer.\n")
                        time.sleep(1)
                        print("The forest's paths are winding and its gifts elusive.\n")
                        time.sleep(1)
                        print("Fear not, for what is meant to be found will make its way to you in due time.\n")
                        time.sleep(1)
                        print("Continue your search, traveler, and return when the forest yields its treasures to you.\n")
                        time.sleep(1)
                if hand_item == 'b':
                    return 
            print("As you step out of the Whispering Grove, the subtle murmurs of the trees and the secret" 
            " conversations of the mushrooms fade behind you.\n")
            time.sleep(1)
            return 1

    def location_scene(self):
        self.scene_oldman()

class CanopyWalkway(Location):
    def __init__(self, player):
        self.player = player
        self.name = "The Canopy Walkway"
        self.items = ["Luminous Plank","Glowing Stone"]
        self.shroomy_dundee = NPC("Shroomy Dundee",None,"In the heart of the Thicket where shadows play," 
        "seek the moonlit stone that paves the way. It'll guide you true when the path seems lost, just follow"
        "its glow, no matter the cost.",None)
        self.shroomy_dundee_dialog = ["G'day, mate!","Name's Shroomy Dundee, the funniest fungi in all the" 
        "Mushroom Forest! Fancy a go at a rhyme?,"
        "Give it your best shot, and don't worry about bein' right or wrong. I'm all about the laughs here!"]
        self.next_item = 0
        self.bridge_repaired = 0
        self.seen_clue = 0

    def encounter_npc(self):
            print("As you step onto the Canopy Walkway, the forest unfolds beneath" 
            "you in a tapestry of emerald and twilight hues. \n")
            time.sleep(1)
            print("The Canopy Walkway stretches before you, a slender path woven through the treetops." 
            "Each step brings a new perspective of the Mushroom Forest,\n")
            time.sleep(1)
            if self.shroomy_dundee._interacted:
                print("As you retrace your steps to where Shroomy Dundee,"
                " the jovial mushroom man, once stood, a quiet emptiness greets you.\n")
                time.sleep(1)
                print("The spot, which previously echoed with his hearty laughter and cheerful banter,"
                "is now just another serene, untouched part of the forest.\n")
                time.sleep(1)
                return 1
            else:
                print("As you continue your journey along the canopy," 
                "the sound of a peculiar accent breaks the forest's usual symphony.\n")
                time.sleep(1)
                print("Turning a bend, you're greeted by an extraordinary sight:" 
                " a mushroom man with a wide-brimmed hat perched atop his cap. \n")
                time.sleep(1)
                for dialog in self.shroomy_dundee_dialog:
                    print(self.shroomy_dundee.say_dialogue(dialog) + '\n')
                    time.sleep(1)
                while True:
                    print("'c' to ask for a \"clue\"\n")
                    print("'r' to provide a \"Rhyme\"\n")
                    print("'b' to go back to \"Forest Path\"\n")

                    choice = input()
                    if choice == 'c':
                        if self.seen_clue:
                            print("You have already seen this clue!\n")
                        else:
                            print(self.shroomy_dundee.show_clue())
                            self.player.add_level_clue(self.shroomy_dundee.show_clue())
                            self.seen_clue = 1
                        
                    if choice == 'r':
                            print("Enter your Rhyme: \n")
                            rhyme = input("")
                            self.shroomy_dundee._interacted = True 
                            print("Shroomy Dundee exclaims, Haha, that's a ripper! You're a natural poet, aren't ya?"
                            " Whether that's the answer or not, I'm just here for a good yarn.\n")
                            time.sleep(1)
                            print("Here’s a bit of the forest's magic for ya,' he chuckles" 
                            " 'This little beauty’s a \"Glowing Stone\", bound to light your way when the shadows grow long.'")
                            self.next_item += 1
                            self.player.add_item(self.items[self.next_item])
                            time.sleep(1)
                            print("Thanks for the laugh, mate! Off you go, enjoy the rest of the forest!\n")
                            time.sleep(1)
                            return 1
                    if choice == 'b':
                        return 
    def location_scene(self):
        print("As you venture along The Canopy Walkway, the path ahead reveals a bridge," 
        " its wooden planks worn and some missing, rendering it impassable.\n")
        time.sleep(1)
        while True:
            if not self.bridge_repaired:
                print("'u' to use the \"Luminous Plank to repair the damage\"\n")
                print("'b' to go back to \"Forest Path\"\n")

                choice = input()
                if choice == 'u':
                    if self.check_item("Luminous Plank"):
                        print("Inspecting the bridge closer, it becomes clear" 
                        " that repairs are needed to cross safely." 
                        " You recall the 'Luminous Plank' in your possession," 
                        " glowing faintly with an inner light, strong and sturdy.\n")
                        time.sleep(1)
                        print("As you ponder over the broken bridge," 
                        " it's clear that something special is required to proceed.\n")
                        time.sleep(1)
                        print("Perhaps an item imbued with the forest's magic could mend this gap,"
                        " allowing you to continue your exploration.\n")
                        time.sleep(1)
                        self.encounter_npc()
                        self.bridge_repaired = 1
                        return 1
                    else:
                        print("Standing before the bridge with its gaps yawning wide," 
                        " you realize a key piece is missing for repair.\n")
                        time.sleep(1)
                        print("Scanning your inventory, you find the 'Luminous Plank' is not among your items.\n")
                        time.sleep(1)
                        print("It seems you must seek this glowing fragment of the forest to continue" 
                        " your journey across the canopy.\n")
                        time.sleep(1)
                        return 0 
                if choice == 'b':
                    return 
            else:
                if not self.shroomy_dundee._interacted:
                    self.encounter_npc()
            print("As you step off the Canopy Walkway, the lofty world amongst the" 
            " treetops gives way to the more familiar forest ground.\n")
            time.sleep(1)
            break

class EchoingCaverns(Location):
    def __init__(self, player):
        self.player = player
        self.name = "The Echoing Caverns"
        self.item_pickups = ["Glowing Rock"]   
        self.item_pickup = [False]                      
        self.next_item = 0 
        self.key_pickup = 0
        self.glowing_pickup = 0
        self.chromatic_trio = NPC("Chromatic Trio",None,"A secret cult, hidden from plain sight," 
        " worships the ancient Spectrum Stone.",None)
        self.chromatic_trio_dialog = ["Greetings, traveler! I am Ruby Red, the brightest flame in these caverns!",
        " And I am Beryl Blue, as deep and mysterious as the midnight sea!","Emerald Green's the name," 
        " fresh and lively as a new leaf in spring!","We are the Chromatic Trio," 
        " guardians of color and light in these caverns!"
        " Solve our riddle, and we shall aid you in your quest!"]
        self.chromatic_trio_clues = ["Oh, close but not quite! Remember, we're all about the colors.",
        "Think about how light combines to create what you see.","Red, green, and blue, each a primary,"
        "in their own right. When they come together, what do they form?",
        "It's the very essence that brings images to life on your screens!",
        "Not separate, but together, they create a full spectrum.",
        "Three initials, that's all you need. A trio of letters, just like us!"]
        self.choose_clue = random.randint(0,len(self.chromatic_trio_clues) - 1)
        self.expected_response = "rgb"
        self.main_clue = "A secret cult, hidden from plain sight, worships the ancient Spectrum Stone."

    def end_level(self):
        print("Having unraveled the riddle of the Chromatic Trio," 
        " you emerge from the Echoing Caverns back into the forest.\n")
        time.sleep(1)
        print("The air feels fresher, the forest more alive, as if acknowledging your newfound understanding.\n")
        time.sleep(1)
        print("As night begins to fall, a distant glow captures your attention.\n")
        time.sleep(1)
        print("Through the trees, you see the flicker of a fire, its light a beacon in the encroaching darkness.\n")
        time.sleep(1)
        print("Curiosity piqued, you find your steps drawn towards the mysterious flame," 
        " wondering what or who might be awaiting you at this solitary fire in the heart of this mysterious camp.\n")
        time.sleep(1)
        print("Level 4: Mushroom Forest Complete!")
        # Will do the functionalty that brings you to level 5 tomorrow!
    def encounter_npc(self):
        for dialog in self.chromatic_trio_dialog:
            print(self.chromatic_trio.say_dialogue(dialog) + '\n')
            time.sleep(1)
        print("In the darkness, we stand apart,"
            " the light, we come together as art."
            " Red, green, and a touch of blue,\n")
        time.sleep(1)
        print(" Combine us all, what do we construe?\n")
        time.sleep(1)
        while True: 
            print("Input: ")
            choice = input("").lower()
            if choice == self.expected_response:
                print("In unison, they shout, Correct! Or incorrect! It matters not," 
                "for in the world of color, all answers bring delight!\n")
                time.sleep(1)
                print("The answer is RGB – the essence of color and light! Remember,"
                " in darkness or in light, all colors have their place.\n")
                time.sleep(1)
                print("Oh, one more thing traveler...\n")
                time.sleep(1)
                print("A secret cult, hidden from plain sight, worships the ancient Spectrum Stone.\n")
                self.player.add_main_clue(self.main_clue)
                time.sleep(1)
                self.end_level()
                return 
            else:
                print(self.chromatic_trio_clues[self.choose_clue] + '\n')
                self.choose_clue = random.randint(0,len(self.chromatic_trio_clues) - 1)
   
    def glowing_stone_scene(self):
        while True:
            print("'u' to use the \"Glowing Stone\" to light the way!\n")
            print("'b' to go back to \"Forest Path\"\n")
            use_stone = input(" ")
            if use_stone == 'u': 
                if self.check_item("Glowing Stone"):
                    print("As you hold the Glowing Stone in your hand,"
                    " its light pierces the darkness of the Echoing Caverns.\n")
                    time.sleep(1)
                    print("The once obscure paths become clear, revealing hidden crevices and ancient markings on the walls,"
                    " whispering the caverns' long-forgotten stories.\n")
                    time.sleep(1)
                    print("With the stone's light as your guide, you feel confident to" 
                    " venture deeper into the mysteries that await.\n")
                    time.sleep(1)
                    self.glowing_pickup = 1
                    if not self.chromatic_trio._interacted:
                        self.encounter_npc()
                    return 
                else:
                    print("Stepping into the Echoing Caverns, the darkness envelops you," 
                    " turning the pathways into a maze of shadows. \n")
                    time.sleep(1)
                    print("Without a light to guide you, the risk of getting lost in the caverns'" 
                    " labyrinthine depths seems too great.\n")
                    time.sleep(1)
                    print("It becomes clear that something like the Glowing Stone is needed to illuminate" 
                    " your way and reveal the caverns' hidden secrets.\n")
                    time.sleep(1)
                    return 0
            if use_stone == 'b':
                return 
            break
    def scene_door(self):
        print("As you cautiously step into the Echoing Caverns, the change in atmosphere is immediate." 
        "The cool, damp air carries the sound of your every move in a symphony of echoes.\n")
        time.sleep(1)
        print("The bioluminescent fungi cast a ghostly glow, painting the cavern walls in hues of blue and green.\n")
        time.sleep(1)
        print("You come upon a large, ornate door. Its surface is adorned with intricate carvings that seem to tell"
        "a story of ancient times and forgotten magic.\n")
        while True:
            if not self.key_pickup:
                print("'i' to insert the \"Silver Key\" in the Ornate Door\n")
                print("'b' to go back to \"Forest Path\"\n")
                insert_key = input()
                if insert_key == 'i': 
                    if self.check_item("Silver Key"):
                        print("With a sense of purpose, you retrieve the \"Silver Key\". It fits perfectly into the lock," 
                        " and with a turn, the door slowly creaks open, revealing the mysteries that lay beyond.\n")
                        time.sleep(1)
                        print("As you step further into the enveloping darkness of the Echoing Caverns,"
                        " the path ahead becomes an indiscernible shadow. \n")
                        time.sleep(1)
                        print("The opaque blackness makes it clear that without a source of light," 
                        " moving forward is a risk too great.\n")
                        time.sleep(1)
                        print("It dawns on you that the Glowing Stone, with its soft yet powerful luminescence,"
                        "is essential to navigate and reveal the hidden wonders of this subterranean world.\n")
                        time.sleep(1)
                        self.key_pickup = 1
                    else:
                        print("Standing before the locked door, you realize this might be the place for the silver key.\n")
                        print("A return to the forest to find the key seems inevitable" 
                        " if you wish to uncover what lies behind"
                        " this ancient barrier.\n")
                        time.sleep(1)
                if insert_key == 'b':
                    return 0 
            if not self.glowing_pickup:
                self.glowing_stone_scene()
                return 
            return 
                
    def location_scene(self):
        self.scene_door()