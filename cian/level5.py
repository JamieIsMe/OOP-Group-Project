from sean.locationClass import Location
from cian.characters import NPC
from cian.Dice_minigame import dice_game
from cian.RPS_minigame import Rock_Paper_Scissors_Game
from denis.Player import Player

class Camp(Location):
    def __init__(self, coins):
        super().__init__("camp",
                         ["outer_camp", "main_camp", "hut_1", "hut_1_inside","big_hut_outside", "big_hut", "side_main_camp"],
                         ["Goblin trio", "Dice Goblin", "Goblin Elder"],
                         [])
        self.current_location = "outer_camp"
        self.visited_sublocations = []
        self.coins = coins
        self.goblin_trio = NPC("Goblin trio",
                               ["\nYou here voices in unison say:\n\"What do you want\"?\n",
                                "You here a high pitched voice from the other side\n\n\"Nobody is home\"!\n",
                                "First Goblin: \"We heard the elder talk about that\nSecond Goblin: \"We dont know nothing\"\n"
                               "Third Goblin: \"The elder should be in the big hut\"\n",
                                "\n\"You are not getting we have the door barred\"!The voices on the other side shout\n"],
                               ["Goblin elder is in the big hut",],
                               "",
                               ["\nThe door opens slightly and you see 3 Goblins peer through the crack nervously\n",
                                "The Goblin trio open the door further and you see 3 identical goblins."
                                "The only difference is their eye colour\n"])

        self.dice_goblin = NPC("Dicy",
                               ["\nShady Goblin: Welcome friend!\nIf im not mistaken you\"re new around here.\nThe names Dicy\n",
                                "\nRecon you fancy a game of dice friend?\n",
                                "\nHow about the ol' rock paper scissors then?\n",
                                "\nHow about another round?\n",
                                "\nWell friend you seem mighty well off "
                                "how abouts i give you some information as a fellow benefactor of life\n",
                                "\nNow dont go spreading this info around\n",
                                "\n\n"],
                               ["Dicy's clue"],
                               "",
                               ["He says as he tips his hat"],)

        self.posh_goblin = NPC("Reginald Thornsworth the Refined",
                               ["\n\"Now, now, Grizzle, we ought to listen to their inquiries. "
                                "Pray, what is it that you seek from the elder, my good fellow?\"\n",
                                "\"Pray, good sir, how may we be of service to you on this occasion?\"\n",
                                "\"I say, old chap, one cannot simply waltz over to have a chat with the elder. "
                                "Pray, enlighten us to what urgent matter compels you to seek an audience with "
                                "such haste and gusto?\"\n",
                                "\"Ah, so you've encountered Snatch, Scratch, and Milo. If they've sent you, my friend, "
                                "it suggests that you are of good character on their part. One could surmise that you "
                                "are not of ill intent, given their commendable judgment in such matters. You may enter\""],
                               ["Goblins trios names are Snatch, Scratch, and Milo"],
                               "",
                               ["His words are adorned with a touch of sophistication, "
                                "making it clear that he sees himself as a goblin of importance."],)

        self.rough_goblin = NPC("Grizzle \"Knuckles\" O'Connor",
                                ["\"Oi, wagwan? You new 'round 'ere or somethin'? State your ends bruv!\"",
                                 "\n\"Yeah, bruv, never clocked that spot, but it don't sound like we got beef with them, "
                                 "ya get me? Anyhows fam, but we can't let you roll up on the elder like that. "
                                 "It's a no-go, ya get me?\"\n",
                                 "\"Look, if you ain't spillin' any details, fam, we ain't just gonna let you slide in like that\"\n"],
                               [],
                               "",
                               ["His speech is laced with even more street slang, and there's a casual confidence"
                                " in his demeanor that suggests he's not one to be messed with. Despite the laid-back"
                                " approach\n",],)

        self.elder_goblin = NPC("Goblin elder",
                               ["\"Take a seat young one tell this old man your tubules\".\nDespite their stature, "
                                "their raspy yet commanding voice exudes wisdom", "\"Tea?\"", "\"So what trubbles such a young soul\""],
                               "",
                               [],
                                ["As you sit he finishes up what he was working on and takes a seat across form you",
                                 "He hops down off of his chair and goes over to the cauldron. With one swift movement "
                                 "he produces a hug and dips it into the bubbling liquid. "
                                 "He returns to you with the tea? and returns to sitting across from you",],)
        self.max_coins = 100

    def outer_camp(self):
        self.current_location = "outer_camp"
        if self.current_location not in self.visited_sublocations :
            print("\nEmerging from the dense forest, you spot a small goblin camp at the foot of towering cliffs. "
                  "Ramshackle huts, constructed from salvaged materials, form a chaotic maze in the shadows. "
                  "Flickering bonfires illuminate the primitive dwellings. "
                  "You spot 3 shadows dart into the nearest hut.\n")
            self.visited("outer_camp")
        else:
            print("You walk back out of the camp and look back at it, Not much has changed\n")

        while self.current_location == "outer_camp":

            choice = input(f"What will you do?\n1) Investigate the first Hut\n2) Walk deeper into the camp\n"
                           "3) Keep observing the camp from outside\n")
            # to 1st hut
            if choice == "1":
                print("As you enter the camp you come to the realisation that you cant see any sign of the residents.")
                self.hut_1()

            # to main camp
            elif choice == "2":
                print("You walk past the first hut and deeper into the town")
                self.main_camp()

            # stay where they are
            elif choice == "3":
                self.outer_camp()

    def hut_1(self):
        self.current_location = "hut_1"
        if self.current_location not in self.visited_sublocations:
            print("You come up to the door of the first hut where you saw the 3 shadows enter\n")

        else:
            print("As you approach the hut you see that the door is open and nobody is inside. "
                  "The goblin trio has left\n"
                  "You walk deeper into the camp\n")
            self.main_camp()

        while self.current_location == "hut_1":
            choice = input("\nWhat will you do?\n1) Knock on the door\n2) Try to open it\n"
                           "3) Walk deeper into the camp\n")
            interacting = True
            if choice == "1":
                print("")
                print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[1]))
                self.visited("hut_1")
                interacting = True
            elif choice == "2":
                print("You try to open the door by force with little success")
                print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[3]))
                interacting = True
            elif choice == "3":
                self.main_camp()

            while interacting:
                choice = input("What will you do?\n1) Say that you just want to talk and you mean no harm\n"
                               "2) Try to open the door\n3) Leave and go further into the town\n")

                if choice == "1":
                    print(self.goblin_trio.actions[0])
                    print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[0]))

                    choice = input("How do you respond?\n1) 'I just wanted to see if you have any information on"
                                   "some missing people'\n2)'Wrong hut sorry'. Leave and go further into the town\n")
                    if choice == "1":
                        print(self.goblin_trio.actions[1])
                        print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[2]))
                        self.add_clue(self.goblin_trio.clues[0])
                        self.visited("hut_1_inside")
                        choice = input("Where will you go next?\n1) Go back to the outside of the camp.\n"
                                       "2) Go deeper into the village to find the elder.\n")
                        if choice == "1":
                            interacting = False
                            self.outer_camp()
                        elif choice == "2":
                            interacting = False
                            self.main_camp()

                    elif choice == "2":
                        interacting = False
                        self.main_camp()

                elif choice == "2":
                    print("You try to open the door by force with little success")
                    print(self.goblin_trio.say_dialogue(self.goblin_trio.dialogue[3]))

                elif choice == "3":
                    interacting = False
                    self.main_camp()

    def main_camp(self):
        self.current_location = "main_camp"
        if self.current_location not in self.visited_sublocations:
            print("You arrive in the center of the camp.\nFrom here you can see the entire camp."
                  "\n\nSome points of interest include:\n"
                  "1. The First Hut\n2. The Big Hut with 2 angry looking goblins guarding the entrance.\n"
                  "3. A Goblin in a long trench coat and large hat "
                  "sitting on the ground with a set of dice in front of him.\n")
            self.visited("main_camp")

        choice = input("\nWhere will you go?\n"
                       "1) Back to the First Hut\n"
                       "2) To the Big Hut\n"
                       "3) Over to the Suspicious Goblin\n"
                       "4) Leave Camp\n")

        if choice == "1":
            self.hut_1()
        elif choice == "2":
            self.big_hut_outside()
        elif choice == "3":
            self.side_main_camp()
        elif choice == "4":
            self.outer_camp()

    def big_hut_outside(self):
        self.current_location = "big_hut_outside"
        if self.current_location not in self.visited_sublocations:
            print("You walk over to the large hut in the center of the camp. "
            "From a distance, you see the curious pair of goblin guards stationed outside a large hut."
            "One, a pint-sized figure, catches your eye with stolen finery and an air of aristocratic pride."
            "His hooked nose supports a tiny monocle."
            "On the flip side, another goblin, rough and untamed, captures your attention. Clad in patchwork leather,"
            "he wields a rusty blade with a menacing air. His body is adorned with crude tattoos depicting goblin mischief,"
            "forming a stark contrast to his posh companion.\n")

            print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[0]))
            input()
            print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[1]))
            print(self.rough_goblin.actions[0])
            print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[0]))
            print(self.posh_goblin.actions[0])
            self.visited("big_hut_outside")

        else:
            print("How can we help you")

        if "hut_1_inside" in self.visited_sublocations:
            choice = input("\nHow do you respond?\n"
                           "1) Go back to camp"
                           "2) Say that you need to talk to the elder\n"
                           "3) Say that you were sent here by the trio of goblins you met earlier")
        else:
            choice = input("\nHow do you respond?\n"
                           "1) Go back to camp\n"
                           "2) Say that you need to talk to the elder\n")

        if choice == "1":
            print("You return to the center of camp\n")
            self.main_camp()
        elif choice == "2":
            print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[1]))

            choice = input("\nWhat do you do?\n"
                           "1) Tell the Truth about what you have learnt?\n"
                           "2) Insist that you cant tell them and you need to talk to the elder\n")
            if choice == "1":
                print("You relay all of the information you have learned so far and emphasis the urgency of your request")
                self.big_hut()
            elif choice == "2":
                print(self.rough_goblin.dialogue[2])
                print(self.rough_goblin.say_dialogue(self.rough_goblin.dialogue[2]))

                print("You return to the center of camp\n")
                self.main_camp()
        elif choice == "3":
            print(self.posh_goblin.say_dialogue(self.posh_goblin.dialogue[3]))
            self.add_clue(self.posh_goblin.clues[0])
            print()

    def big_hut(self):
        self.current_location = "big_hut"
        if self.current_location not in self.visited_sublocations:
            self.visited("side_main_camp")
            print("The goblin elder's hut is a cozy chaos of logs, vines, and scattered belongings. A bubbling cauldron"
                  " in one corner scents the air, while a central fire pit lights up a cluttered table with maps and"
                  " trinkets. Mismatched furniture surrounds the fire, and tapestries tell the tribe's stories Despite "
                  "the disorder, there's a communal atmosphere, reflecting the practical and resourceful nature of "
                  "goblin living.\n In the corner of the room working on a fesh tapestrie is the goblin elder\n")
            print("The goblin elder, hunched with age, wears a tattered hood and bears tribal markings on a "
                  "weathered face. Sharp, intelligent eyes gleam from under strands of gray hair. "
                  "Adorned in earth-toned garments, the elder carries a staff adorned with feathers and symbols.\n ")

            print("without turning around the Elder addresses you")
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[0]))
            print(self.elder_goblin.actions[0])
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[1]))
            print(self.elder_goblin.actions[1])
            print(self.elder_goblin.say_dialogue(self.elder_goblin.dialogue[2]))




    def side_main_camp(self, coins=100):
        self.current_location = "side_main_camp"
        if self.current_location not in self.visited_sublocations:
            print("You walk over to the Shady Goblin\n")
            print(self.dice_goblin.dialogue[0])
            print(self.dice_goblin.actions[0])
            self.visited("side_main_camp")

        if coins == self.max_coins:
            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[4]))
            self.add_clue(self.dice_goblin.clues[0])
            self.review_clues()
            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[5]))

        print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[1]))
        play_minigame = True
        while play_minigame:
            choice = input("1) Yes\n2) No\n")
            if choice == "1":
                dice_game()
            elif choice == "2":
                print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[2]))
                choice = input("1) Yes\n2) No\n")
                if choice == "1":
                    Rock_Paper_Scissors_Game()
                    play_minigame = True
                else:
                    break

            print(self.dice_goblin.say_dialogue(self.dice_goblin.dialogue[3]))
            choice = input("1) Yes\n2) No\n")
            if choice == "1":
                dice_game()
            elif choice == "2":
                print("You decline and return to the center of camp")
                break
        self.main_camp()




if __name__ == "__main__":
    camp = Camp(0)
    camp.outer_camp()
