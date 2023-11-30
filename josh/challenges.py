import random
from max.minigame import cipher_decryption_game

class LibraryGame:
    def __init__(self):
        self.books = {
            "Mystery Book": "Solve a riddle!",
            "Puzzle Book": "Solve a Logical Puzzle",
            "History Book": "Answer a historical trivia question!",

        }

    def book_roulette(self):
        print(f"David the Druid: Welcome to the Book Roulette! A book will be chosen and face the challenge.")
        print("There are 3 Book, and the book toy will recieve is random!, Solve the Puzzle to advance to the final challenge!")
        chosen_book = random.choice(list(self.books.keys()))
        print(f"You have picked up '{chosen_book}'.")
        print(f"Challenge: {self.books[chosen_book]}")

        # Implement logic to handle different challenges based on the chosen book
        if chosen_book == "Mystery Book":
            self.solve_riddle()
        elif chosen_book == "Puzzle Book":
            self.solve_puzzle()
        elif chosen_book == "History Book":
            self.history_trivia()


    def solve_riddle(self):
        # Implement logic for the riddle challenge
        print("You open the Mystery Book, and a,  riddle is revealed:")


        riddle = "What has to be broken before you can use it?"


        print(f"Riddle: {riddle}")
        print("1. Egg \n2. Glass \n3. Heart")
        while True:
            # Get the player's answer
            player_answer = input("Your answer : ").lower()

            # Check if the player's answer is correct
            if player_answer.lower() == "Egg" or '1':
                print("Congratulations! You've solved the puzzle!, here is 3 more coins")

                break
            else:
                print("Unfortunately, that's not the correct answer. Keep trying!")


    def solve_puzzle(self):
        # Implement logic for the coding challenge
        print("You chose the Puzzle Book")
        print("Here is your puzzle")
        cipher_decryption_game()
        print("You have Completed my Cipher Puzzle, 3 coins have been awarded to your coin bank")


    def history_trivia(self):
        # Implement logic for the history trivia challenge
        print("The History Book presents you with a historical trivia question. Can you answer it?")
        trivia = "Which Medieval European Kingdom was known for its legendary kings, King Arthur?"
        print(f"Your Question is :{trivia}")
        print("1. France \n2. Spain \n3. England")
        while True:
            # Get the player's answer
            player_answer = input("Your answer : ").lower()

            # Check if the player's answer is correct
            if player_answer.lower() == "england" or '3':
                print("Congratulations! You've solved the trivia question!, here is 3 more coins")
                break
            else:
                print("Unfortunately, that's not the correct answer. Keep trying!")


