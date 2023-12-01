from sean.locationClass import Location
from cian.characters import NPC
from cian.Dice_minigame import dice_game
from cian.RPS_minigame import Rock_Paper_Scissors_Game
from denis.Player import Player

import time
import pygame

class Level5(Location):
    def __init__(self, player):
        super().__init__("camp",
                         ["outer_camp", "main_camp", "hut_1", "hut_1_inside", "big_hut_outside", "big_hut",
                          "side_main_camp", "grave"],
                         ["Goblin trio", "Dice Goblin", "Goblin Elder"],
                         [])
        self.current_location = "outer_camp"
        self.visited_sublocations = []
        self.player = player
        self.goblin_trio = NPC("Goblin trio",
                               ["\nYou here voices in unison say:\n\"What do you want\"?\n",
                                "You here a high pitched voice from the other side\n\n\"Nobody is home\"!\n",
                                "First Goblin: \"We heard the elder talk about that\n"
                                "Second Goblin: \"We dont know nothing\"\n"
                                "Third Goblin: \"The elder should be in the big hut\"\n",
                                "\n\"You are not getting we have the door barred\""
                                "!The voices on the other side shout\n"],
                               ["Goblin elder is in the big hut", ],
                               "",
                               ["\nThe door opens slightly and you see 3 Goblins peer through the "
                                "crack nervously\n",
                                "The Goblin trio open the door further and you see 3 identical goblins."
                                "The only difference is their eye colour\n"])

        self.dice_goblin = NPC("Dicy",
                               [
                                   "\nShady Goblin: Welcome friend!\nIf im not mistaken you\"re new around here."
                                   "\nThe names Dicy\n",
                                   "\nRecon you fancy a game of dice friend?\n",
                                   "\nHow about the ol' rock paper scissors then?\n",
                                   "\nHow about another round?\n",
                                   "\nWell friend you seem mighty well off "
                                   "how abouts i give you some information as a fellow benefactor of life\n",
                                   "\nNow dont go spreading this info around\n",
                                   "\n\n"],
                               ["98% of gamblers give up before they win big"],
                               "",
                               ["He says as he tips his hat"], )

        self.posh_goblin = NPC("Reginald Thornsworth the Refined",
                               ["\n\"Now, now, Grizzle, we ought to listen to their inquiries. "
                                "Pray, what is it that you seek from the elder, my good fellow?\"\n",
                                "\"Pray, good sir, how may we be of service to you on this occasion?\"\n",
                                "\"I say, old chap, one cannot simply waltz over to have a chat with the elder. "
                                "Pray, enlighten us to what urgent matter compels you to seek an audience with "
                                "such haste and gusto?\"\n",
                                "\"Ah, so you've encountered Snatch, Scratch, and Rodrick. If they've sent you, my "
                                "friend, "
                                "it suggests that you are of good character on their part. One could surmise that you "
                                "are not of ill intent, given their commendable judgment in such matters. "
                                "You may enter\"\n"],
                               ["Goblins trios names are Snatch, Scratch, and Rodrick"],
                               "",
                               ["His words are adorned with a touch of sophistication, "
                                "making it clear that he sees himself as a goblin of importance.\n"], )

        self.rough_goblin = NPC("Grizzle \"Knuckles\" O'Connor",
                                ["\"Oi, wagwan? You new 'round 'ere or somethin'? State your ends bruv!\"",
                                 "\n\"Yeah, bruv, never clocked that spot, but it don't sound like we got "
                                 "beef with them, "
                                 "ya get me? Anyhows fam, but we can't let you roll up on the elder like that. "
                                 "It's a no-go, ya get me?\"\n",
                                 "\"Look, if you ain't spillin' any details, fam, we ain't just gonna "
                                 "let you slide in like that\"\n",
                                 "\"Yo fam! good to see ya fam!\"\n"],
                                [],
                                "",
                                ["His speech is laced with even more street slang, and there's a casual confidence"
                                 " in his demeanor that suggests he's not one to be messed with. Despite the laid-back"
                                 " approach\n", ], )

        self.elder_goblin = NPC("Goblin elder",
                                ["\"Take a seat young one tell this old man your tubules\".\nDespite their stature, "
                                 "their raspy yet commanding voice exudes wisdom\n", "\"Tea?\"",
                                 "\"So what troubles such a young soul\"\n",
                                 "\"I have heard may rumors in my 10 long years of life but i have to admit that"
                                 "i have not heard about any cults in this area\"\n",
                                 "\"Now that you mention it i have heard that name somewhere before.... "
                                 "now when was it? Oh yes that was it i believe that i saw that name written on a "
                                 "grave just to the east of camp when i was but a young goblin, what was it 5 years "
                                 "ago. I was lively back then the elder at the time said that i was the most energetic "
                                 "goblin he had ever seen. Look at me getting distracted reminiscing on the past, "
                                 "where was I?.... ah yes the grave its just east of here next to a large oak tree"
                                 " and a cave.\"\n"],
                                ["The Legendary Witch Slayers grave is to the east of camp beside a large tree"],
                                "",
                                ["As you sit he finishes up what he was working on and takes a seat across form you\n",
                                 "He hops down off of his chair and goes over to the cauldron. With one swift movement "
                                 "he produces a hug and dips it into the bubbling liquid. "
                                 "He returns to you with the tea? and returns to sitting across from you\n",
                                 "he looks at you with a bit of disappointment\n"], )
        self.max_coins = 100  # coins needed to set of Dicy's bonus dialog
        self.grave_found = False  # has gained info on the graves location


    def level_start(self):
        self.outer_camp()

    def play(self):
        pygame.mixer.music.load("Kung Fu Panda - Master Oogway Suite (Theme).mp3")
        pygame.mixer.music.play(loops=0)#
        print("\nTEST\n")

    def outer_camp(self):  # outer camp location used as a secondary hub and as an intro
        self.current_location = "outer_camp"
        if self.current_location not in self.visited_sublocations:  # if you haven't been here before
            self.visited("outer_camp")
            print("\nEmerging from the dense forest, you spot a small goblin camp at the foot of towering cliffs. "
                  "Ramshackle huts, constructed from salvaged materials, form a chaotic maze in the shadows. "
                  "Flickering bonfires illuminate the primitive dwellings. "
                  "You spot 3 shadows dart into the nearest hut.\n")
            time.sleep(5)
        else:
            print("You walk back out of the camp and look back at it, Not much has changed\n")

        while self.current_location == "outer_camp":
            if self.grave_found:  # if info on the grave was found in the big hut
                print("-------------------------------------------------------\n")
                choice = input("What will you do?\n"
                               "1) Investigate the first Hut\n"
                               "2) Walk deeper into the camp\n"
                               "3) Keep observing the camp from outside\n"
                               "4) Head east to the grave of The Legendary Witch Slayer\n")
                print("-------------------------------------------------------\n")
                if choice == "1":  # Investigate the first Hut
                    print("As you enter the camp you come to the realisation that you cant see any sign of the "
                          "residents.")
                    self.hut_1()  # sends to location
                # to main camp
                elif choice == "2":  # Walk deeper into the camp
                    print("You walk past the first hut and deeper into the town")
                    self.main_camp()
                # stay where they are
                elif choice == "3":  # Keep observing the camp from outside
                    self.outer_camp()
                elif choice == "4":  # Head east to the grave of The Legendary Witch Slayer
                    self.grave()

            else:
                print("-------------------------------------------------------\n")
                choice = input("What will you do?\n"
                               "1) Investigate the first Hut\n"
                               "2) Walk deeper into the camp\n"
                               "3) Keep observing the camp from outside\n")
                print("-------------------------------------------------------\n")
                # to 1st hut
                if choice == "1":  # Investigate the first Hut
                    print("As you enter the camp you come to the realisation that you cant see any sign of the "
                          "residents.")
                    self.hut_1()
                # to main camp
                elif choice == "2":  # Walk deeper into the camp
                    print("You walk past the first hut and deeper into the town")
                    self.main_camp()
                # stay where they are
                elif choice == "3":  # Keep observing the camp from outside
                    self.outer_camp()

    def hut_1(self):  # first location where you meet the goblin trio and find ot where the elder is
        self.current_location = "hut_1"
        if self.current_location not in self.visited_sublocations:  # if not visited before
            print("You come up to the door of the first hut where you saw the 3 shadows enter\n")

        else:  # shows aftermath of first interaction if you return
            print("As you approach the hut you see that the door is open and nobody is inside. "
                  "The goblin trio has left\n"
                  "You walk deeper into the camp\n")
            self.main_camp()

        while self.current_location == "hut_1":
            print("-------------------------------------------------------\n")

            choice = input("\nWhat will you do?\n"
                           "1) Knock on the door\n"
                           "2) Try to open it\n"
                           "3) Walk deeper into the camp\n")
            print("-------------------------------------------------------\n")

            interacting = True  # marks them as being talked to far the purpose of a loop
            if choice == "1":  # Knock on the door
                print("")
                print(self.goblin_trio.dialogue[1])  # Nobody is home dialogue with no name
                self.visited("hut_1")
                interacting = True
            elif choice == "2":  # Try to open it
                print("You try to open the door by force with little success")
                print(self.goblin_trio.dialogue[3])  # door barred dialogue with no name
                interacting = True
            elif choice == "3":  # Walk deeper into the camp
                self.main_camp()

            while interacting:
                print("-------------------------------------------------------\n")

                choice = input("What will you do?\n"
                               "1) Say that you just want to talk and you mean no harm\n"
                               "2) Try to open the door\n"
                               "3) Leave and go further into the town\n")
                print("-------------------------------------------------------\n")

                if choice == "1":  # Say that you just want to talk and you mean no harm
                    print(self.goblin_trio.actions[0])  # The door opens slightly action
                    print(self.goblin_trio.dialogue[0])  # What do you want dialogue with name

                    print("-------------------------------------------------------\n")
                    choice = input("How do you respond?\n"
                                   "1) 'I just wanted to see if you have any information on"
                                   "some missing people'\n"
                                   "2)'Wrong hut sorry'. Leave and go further into the town\n")
                    print("-------------------------------------------------------\n")
                    if choice == "1":  # 'I just wanted to see if you have any information on some missing people'
                        print(self.goblin_trio.actions[1])  # door opens more action
                        print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[2]))  # elder location dialogue
                        self.add_clue(self.goblin_trio.clues[0])  # adds the location clue "where the elder is"
                        print(self.review_clues(), "\n")  # displays clues
                        self.visited("hut_1_inside")  # mark as success for later dialogue
                        print("-------------------------------------------------------\n")
                        choice = input("Where will you go next?\n"
                                       "1) Go back to the outside of the camp.\n"
                                       "2) Go deeper into the village to find the elder.\n")
                        print("-------------------------------------------------------\n")
                        if choice == "1":  # Go back to the outside of the camp.
                            interacting = False  # no longer taking to them
                            self.outer_camp()
                        elif choice == "2":  # Go deeper into the village to find the elder.
                            interacting = False
                            self.main_camp()

                    elif choice == "2":  # 'Wrong hut sorry'. Leave and go further into the town
                        interacting = False
                        self.main_camp()

                elif choice == "2":  # Try to open the door
                    print("You try to open the door by force with little success")
                    print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[3]))  # door barred dialogue

                elif choice == "3":  # Leave and go further into the town
                    interacting = False
                    self.main_camp()

    def main_camp(self):  # main hub location used to get too and from other locations with NPCs / Clues
        self.current_location = "main_camp"
        if self.current_location not in self.visited_sublocations:
            print("You arrive in the center of the camp.\nFrom here you can see the entire camp."
                  "\n\nSome points of interest include:\n"
                  "1. The First Hut\n2. The Big Hut with 2 angry looking goblins guarding the entrance.\n"
                  "3. A Goblin in a long trench coat and large hat "
                  "sitting on the ground with a set of dice in front of him.\n")
            self.visited("main_camp")
        print("-------------------------------------------------------\n")
        choice = input("\nWhere will you go?\n"
                       "1) Back to the First Hut\n"
                       "2) To the Big Hut\n"
                       "3) Over to the Suspicious Goblin\n"
                       "4) Leave Camp\n")
        print("-------------------------------------------------------\n")

        if choice == "1":  # Back to the First Hut
            self.hut_1()
        elif choice == "2":  # To the Big Hut
            self.big_hut_outside()
        elif choice == "3":  # Over to the Suspicious Goblin
            self.side_main_camp()
        elif choice == "4":  # Leave Camp
            self.outer_camp()

    def big_hut_outside(self):  # used to get into the big hut and is where you interact with the guards
        self.current_location = "big_hut_outside"
        if self.current_location not in self.visited_sublocations:
            print("You walk over to the large hut in the center of the camp. "
                  "From a distance, you see the curious pair of goblin guards stationed outside a large hut."
                  "One, a pint-sized figure, catches your eye with stolen finery and an air of aristocratic pride."
                  "His hooked nose supports a tiny monocle."
                  "On the flip side, another goblin, rough and untamed, captures your attention. Clad in patchwork "
                  "leather, he wields a rusty blade with a menacing air. His body is adorned with crude tattoos "
                  "depicting goblin mischief, forming a stark contrast to his posh companion.\n")

            print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[0]))  # new round here dialogue
            input()  # ask for meaningless input for fun
            print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[1]))  # cant let you in dialogue
            print(self.rough_goblin.actions[0])  # description of speech pattern
            print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[0]))  # why need to talk to elder dialogue
            print(self.posh_goblin.actions[0])  # description of speech pattern
            self.visited("big_hut_outside")

        if "big_hut" not in self.visited_sublocations:
            if "hut_1_inside" in self.visited_sublocations:  # adds option if you interacted with the goblin trio
                print("-------------------------------------------------------\n")
                choice = input("\nHow do you respond?\n"
                               "1) Go back to camp\n"
                               "2) Say that you need to talk to the elder\n"
                               "3) Say that you were sent here by the trio of goblins you met earlier\n")
                print("-------------------------------------------------------\n")

            else:
                print("-------------------------------------------------------\n")
                choice = input("\nHow do you respond?\n"
                               "1) Go back to camp\n"
                               "2) Say that you need to talk to the elder\n")
                print("-------------------------------------------------------\n")

            if choice == "1":  # Go back to camp
                print("You return to the center of camp\n")
                self.main_camp()
            elif choice == "2":  # Say that you need to talk to the elder
                print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[1]))  # how can we help dialogue
                print("-------------------------------------------------------\n")
                choice = input("\nWhat do you do?\n"
                               "1) Tell the Truth about what you have learnt?\n"
                               "2) Insist that you cant tell them and you need to talk to the elder\n")
                print("-------------------------------------------------------\n")
                if choice == "1":  # Tell the Truth about what you have learnt?
                    print(
                        "You relay all of the information you have learned so far and emphasis the urgency of your "
                        "request")
                    self.big_hut()
                elif choice == "2":  # Insist that you cant tell them and you need to talk to the elder
                    print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[2]))  # cant let you in dialogue

                    print("You return to the center of camp\n")
                    self.main_camp()
            elif choice == "3":  # Say that you were sent here by the trio of goblins you met earlier
                print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[3]))  # spoken to the trio dialogue
                self.add_clue(self.posh_goblin.clues[0])  # add goblin trios names to location clues
                print(self.review_clues(), "\n")  # displays clues
                self.big_hut()
        else:
            print("Both guards step aside as you approch")
            print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[3]))  # good to see you again dialogue
            self.big_hut()

    def big_hut(self, ):  # used to interact with the goblin elder
        self.current_location = "big_hut"
        if self.current_location not in self.visited_sublocations:
            self.visited("big_hut")
            print("The goblin elder's hut is a cozy chaos of logs, vines, and scattered belongings. A bubbling cauldron"
                  " in one corner scents the air, while a central fire pit lights up a cluttered table with maps and"
                  " trinkets. Mismatched furniture surrounds the fire, and tapestries tell the tribe's stories Despite "
                  "the disorder, there's a communal atmosphere, reflecting the practical and resourceful nature of "
                  "goblin living.\n In the corner of the room working on a fresh tapestry is the goblin elder\n")
            print("The goblin elder, hunched with age, wears a tattered hood and bears tribal markings on a "
                  "weathered face. Sharp, intelligent eyes gleam from under strands of gray hair. "
                  "Adorned in earth-toned garments, the elder carries a staff adorned with feathers and symbols.\n ")
        else:
            print("As you enter\n")
        print("Without turning around the Elder addresses you\n")
        print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[0]))  # how can I help dialogue
        print(self.elder_goblin.actions[0])  # sits on chair action
        print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[1]))  # Tea?
        print("-------------------------------------------------------\n")
        choice = input("1) Yes\n"
                       "2) No\n")
        print("-------------------------------------------------------\n")
        if choice == "1":  # Yes
            print(self.elder_goblin.actions[1])  # get tea action
        elif choice == "2":  # No
            print(self.elder_goblin.actions[2])  # disappointment action

        print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[2]))  # what troubles you dialogue
        interacting = True
        while interacting:
            print("-------------------------------------------------------\n")
            choice = input("What would you like to ask the elder?\n"
                           "1) Do you know anything about a cult that is kidnapping people?\n"
                           "2) Have you heard of \"The Legendary Witch Slayer\n"
                           "3) Leave the large hut\n")
            print("-------------------------------------------------------\n")

            if choice == "1":  # Do you know anything about a cult that is kidnapping people?
                print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[3]))  # not heard anything dialogue
            elif choice == "2":  # have you heard of The Legendary Witch Slayer
                print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[4]))  # seen grave dialogue
                self.add_clue(self.elder_goblin.clues[0])  # add grave location to clues
                print(self.review_clues(), "\n")  # display clues
                self.grave_found = True  # mark as location found to open up choice in Outer camp
            elif choice == "3":  # Leave the large hut
                interacting = False  # no longer interacting

        self.main_camp()

    def side_main_camp(self, ):  # used to interact with dice goblin and mini-games can give set coins to start
        self.current_location = "side_main_camp"
        if self.current_location not in self.visited_sublocations:
            print("You walk over to the Shady Goblin\n")
            print(self.dice_goblin.dialogue[0])  # welcome dialogue no name
            print(self.dice_goblin.actions[0])  # Tips hat action no name
            self.visited("side_main_camp")

        if self.player.coins == self.max_coins:  # if you have alot of coins he gives you a bit of info and an item
            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[4]))  # why give item dialogue
            self.add_clue(self.dice_goblin.clues[0])  # adds clue to location clues
            print(self.review_clues(), "\n")  # displays clues so far
            self.player.add_item("1 gold doubloon")  # adds item to player
            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[5]))  # don't tell anyone else dialogue

        print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[1]))  # play dice minigame dialogue
        play_minigame = True
        while play_minigame:
            print("-------------------------------------------------------\n")
            choice = input("1) Yes\n"
                           "2) No\n")
            print("-------------------------------------------------------\n")
            if choice == "1":  # Yes
                dice_game(self.player)  # plays dice minigame
            elif choice == "2":  # No
                print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[2]))  # play R.P.S. minigame dialogue
                print("-------------------------------------------------------\n")
                choice = input("1) Yes\n"
                               "2) No\n")
                print("-------------------------------------------------------\n")
                if choice == "1":  # Yes
                    Rock_Paper_Scissors_Game(self.player)  # plays R.P.S. minigame
                    play_minigame = True
                elif choice == "2":  # No
                    self.main_camp()

            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[3]))  # play again dialogue
            print("-------------------------------------------------------\n")
            choice = input("1) Yes\n"
                           "2) No\n")
            print("-------------------------------------------------------\n")
            if choice == "1":  # Yes
                dice_game(self.player)
            elif choice == "2":  # No
                print("You decline and return to the center of camp")
                break
        self.main_camp()

    def grave(self):  # used to observe and investigate the grave and to lead to the cave/end
        self.current_location = "grave"
        if self.current_location not in self.visited_sublocations:
            self.visited("grave")
            print("At the base of a sprawling ancient oak tree rests The Legendary Witch Slayer's grave. "
                  "The weathered tombstone bears a symbol of a crossed sword and broomstick, marking the hero's final "
                  "battles against darkness. Moss-covered and surrounded by the quiet embrace of nature, the site is "
                  "near a mysterious cave entrance—the backdrop to the hero's last epic confrontation. Shadows dance "
                  "as daylight filters through ancient branches, creating an aura of reverence. The air whispers with "
                  "the hero's legacy, ensuring their tale endures in the heart of the enchanted forest.")
        print("-------------------------------------------------------\n")
        choice = input("What will you do?\n"
                       "1) Investigate the Grave closer\n"
                       "2) Sit by the grave for a while\n"
                       "3) Investigate the Cave\n"
                       "4) return to camp\n")
        print("-------------------------------------------------------\n")
        if choice == "1":  # Investigate the Grave closer
            print("As you inspect the grave further you spot a scrap of red cloth stuck to a particularly rough part")
            if "The Legendary Witch Slayer will save us all message" in self.player.main_clues:
                print("You remember that this is the same cloth that the cultists wear\n")
                print("You think to yourself why would this be here on a heroes grave?\n")
                self.player.add_main_clue("The Legendary Witch Slayer might not be what they seem to be in the legends")
                self.player.add_item("Red scrap of cloth")
            else:
                print("You recognise this cloth but you cant quite remember where")
            self.grave()
        elif choice == "2":  # Sit by the grave for a whileself.play()
            self.play()
            print("As you decide to sit by the grave of The Legendary Witch Slayer, time takes on a different cadence "
                  "in this tranquil and sacred place. The gentle rustling of leaves overhead creates a soothing melody "
                  "as sunlight filters through the dense canopy, casting dappled patterns on the moss-covered ground."
                  "\n The air carries a subtle fragrance of earth and flowers, blending seamlessly with the distant "
                  "murmur of a crystal-clear stream nearby. Small woodland creatures, curious yet unafraid, venture "
                  "closer to investigate the visitor who has entered their realm.\n As minutes turn into moments, the "
                  "atmosphere becomes more charged with an otherworldly energy. Shadows playfully dance around the "
                  "grave, seemingly animated by the spirits of the forest. The engraved symbol on the weathered "
                  "tombstone glows softly as if reflecting the hero's enduring presence.\n In the distance, the "
                  "mysterious cave entrance stands as a silent gateway to untold secrets, occasionally revealing hints "
                  "of magical whispers and ancient echoes. The great oak tree above sways gently in response to a "
                  "breeze, its leaves creating a gentle, melodic rustle—a natural symphony that serenades you in your "
                  "contemplation.\n As you sit in quiet reflection, a feeling of connection to the hero's legacy "
                  "permeates the air, bridging the gap between the past and the present. Whether it's the subtle shift "
                  "of sunlight or the occasional fluttering of a butterfly, every detail seems to carry a deeper "
                  "meaning in this hallowed grove. You, immersed in the tranquillity of the moment, may sense a subtle "
                  "reassurance—a reminder that even in stillness, the legends of heroes endure.\n")
            self.grave()
        elif choice == "3":  # Investigate the Cave
            print("Before you stands the cave mouth framed by moss-covered rocks and veiled in vines."
                  " It beckons with a mysterious allure, its entrance wide and dark, inviting you to explore its "
                  "depths. The shadows within suggest untold secrets, while a gentle breeze whispers the promise of "
                  "undiscovered mysteries concealed within its confines.\n")
            print("As you look closer you notice that there are quite a few fresh footprints in the dirt")
            print("-------------------------------------------------------\n")
            choice = input("What will you do?\n"
                           "1) Enter the cave\n"
                           "2) Go back to the grave\n")
            print("-------------------------------------------------------\n")

            if choice == "1":  # Enter the cave
                pass
            elif choice == "2":  # Go back to the grave
                self.grave()
        elif choice == "4":  # return to camp
            print("You leave the grave and return to the center of the camp\n")
            self.main_camp()


if __name__ == "__main__":
    player = Player("Player Name")
    camp = Level5(0)
    camp.outer_camp()
