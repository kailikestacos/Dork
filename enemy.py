class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2
        self.alive_text = "sample text"
        self.dead_text = "sample text"

class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 30
        self.damage = 10
        self.alive_text = "sample text"
        self.dead_text = "sample text"

class BatColony(Enemy):
    def __init__(self):
        self.name = "Colony of Bats"
        self.hp = 100
        self.damage = 4
        self.alive_text = "sample text"
        self.dead_text = "sample text"

class Rockmonster(Enemy):
    def __init__(self):
        self.name = "Rock Monster"
        self.hp = 80
        self.damage = 15
        self.alive_text = "sample text"
        self.dead_text = "sample text"