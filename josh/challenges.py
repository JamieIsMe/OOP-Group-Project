import random
from level1 import Level1

class LibraryGame:
    def __init__(self):
        self.books = {
            "Mystery Book": "Solve a riddle!",
            "Puzzle Book": "Solve a Logical Puzzle",
            "History Book": "Answer a historical trivia question!",

        }

    def book_roulette(self):
        print(f"David the Druid: Welcome to the Book Roulette! A book will be chosen and face the challenge.")
        chosen_book = random.choice(list(self.books.keys()))
        print(f"You picked up '{chosen_book}'.")
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
        print("You open the Mystery Book, and a medieval riddle is revealed:")

        # Add your Medieval Riddle here
        riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"

        print(f"Riddle: {riddle}")

        # Get the player's answer
        player_answer = input("Your answer: ").lower()

        # Check if the player's answer is correct
        if player_answer == "an echo":
            print("Congratulations! You've solved the Medieval Riddle!")
        else:
            print("Unfortunately, that's not the correct answer. Keep trying!")


    def solve_puzzle(self):
        # Implement logic for the coding challenge
        print("You chose the Puzzle Book")


    def history_trivia(self):
        # Implement logic for the history trivia challenge
        print("The History Book presents you with a historical trivia question. Can you answer it?")


