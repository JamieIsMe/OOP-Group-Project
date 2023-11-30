from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, dialogue, clue, item, action):
        self.name = name
        self._dialogue = dialogue
        self._interacted = False
        self.clues = clue
        self._items = item
        self._actions = action

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
            interaction = f"{self.name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"You have already talked to {self.name}"

        return interaction

    # def items(self):
    # pass
    # add item to player from NPC

    def clue(self):
        pass
        # add clue to clue list from NPC

    @property
    def dialogue(self):
        return self._dialogue

    @property
    def items(self):
        return self._items

    @property
    def actions(self):
        return self._actions


# This class has not changed in this lab
class NPC(Character):
    """
    A class that implements the abstract class Character.
    The perform_action method must provide logic.
    The purpose of this class is to provide characters that are not
    essential for the mystery.
    """

    def perform_action(self, action):
        return f"{self.name} {action}."

    def say_dialogue(self, dialogue):
        return f"{self.name}: {dialogue}."

    def interact(self):
        interact = super().interact()
        return interact

    def clue(self):
        return self.clues
