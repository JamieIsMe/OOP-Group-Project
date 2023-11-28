import time
def MedievalPuzzle():
    print("The Druid presents you with a medieval puzzle:")
    time.sleep(2)
    print("In days of old, when knights were bold,")
    print("And kings roamed the land untold,")
    time.sleep(1)
    print("To prove thy might and gain the tools,")
    print("Answer me this riddle, and you'll be equipped...:")
    print("")
    print("I speak without a mouth and hear without ears.")
    print("I have no body, but I come alive with the wind.")
    print("What am I?")

    correct_answer = "echo"
    attempts = 0

    while attempts < 3:
        player_answer = input("Your answer: ").lower()

        if player_answer == correct_answer:
            print("Well done! The Druid nods in approval.")
            print("I now bestow upon you the Chaos Sword.")


            return True
        else:
            attempts += 1
            print("Incorrect. The Druid looks thoughtful.")
            print(
                f"You have {3 - attempts} {'tries' if (3 - attempts) > 1 else 'try'} left.")

    print("The Druid sighs.")
    print("It seems this quest may be too challenging for you.")