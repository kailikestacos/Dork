class Quest:
    def __init__(self):
        raise NotImplementedError("Do not create raw quests")

    def __str__(self):
        return self.name


class StartingOut(Quest):
    def __init__(self):
        self.name = "Starting Out"
