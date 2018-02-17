import items
import quests


class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.scrap = 100
        self.inventory = [items.Medkit()]

class Sam(NonPlayableCharacter):
    def __init__(self):
        self.name = "Sam"
        self.quests = [quests.StartingOut]