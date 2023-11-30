from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, dialogue, clue, item, action):
        self.name = name
        self.dialogue = dialogue
        self._interacted = False
        self.clues = clue
        self.items = item
        self.actions = action

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self.name < other.name
        return False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self, action):
        pass

    @abstractmethod
    def say_dialogue(self, dialogue):
        pass

    def interact(self):
        if not self._interacted:
            interaction = f"{self.name}: {self.dialogue}"
            self._interacted = True
        else:
            interaction = f"You have already talked to {self.name}"

        return interaction

    def clue(self):
        pass
        # add clue to clue list from NPC

    def dialogue(self):
        return self.dialogue

    def items(self):
        return self.items

    def actions(self):
        return self.actions


class NPC(Character):

    def perform_action(self, action):
        return f"{self.name} {action}."

    def say_dialogue(self, dialogue):
        return f"{self.name}: {dialogue}"

    def interact(self):
        interact = super().interact()
        return interact

    def clue(self):
        return self.clues
