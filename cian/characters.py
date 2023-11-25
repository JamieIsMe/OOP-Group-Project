from abc import ABC,abstractmethod

class Character(ABC):
    def __init__(self, name, dialogue , clue, item ):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False
        self.clues = clue
        self.items = item

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self._name == other._name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self._name < other._name
        return False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self, action):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.
    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"You have already talked to {self._name}"

        return interaction

    def items(self):
        pass
            # add item to player from NPC

    def clue(self):
        pass
            # add clue to clue list from NPC



# This class has not changed in this lab
class NPC(Character):
    """
    A class that implements the abstract class Character.
    The perform_action method must provide logic.
    The purpose of this class is to provide characters that are not
    essential for the mystery.
    """
    def perform_action(self, action):
        return f"{self._name} {action}."

    def interact(self):
        super().interact()

