import random
import items


class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Exterminator(Enemy):
    def __init__(self):
        r = random.random()
        if r <= 0.5:
            self.weapon = items.PristinePlasmaPistol()
        elif r <= 0.6:
            self.weapon = items.PristinePlasmaAxe()
        elif r <= 0.7:
            self.weapon = items.PristinePlasmaSword()
        elif r <= 1.0:
            self.weapon = items.PristinePlasmaRifle()
        self.name = "{} Exterminator".format(self.weapon.name)
        self.hp = 65
        self.damage = self.weapon.damage
        self.xp = 30
        self.scrap = 25
        self.dodge = 0.85


class ExterminatorOld(Enemy):
    def __init__(self):
        r = random.random()
        if r <= 0.5:
            self.weapon = items.SalvagedPlasmaPistol()
        elif r <= 0.6:
            self.weapon = items.SalvagedPlasmaAxe()
        elif r <= 0.7:
            self.weapon = items.SalvagedPlasmaSword()
        elif r <= 1.0:
            self.weapon = items.SalvagedPlasmaRifle()

        self.name = "Scrappy {} Exterminator".format(self.weapon.name)
        self.hp = 30
        self.damage = self.weapon.damage
        self.xp = 25
        self.scrap = 15
        self.dodge = 0.9



class MutatedDog(Enemy):
    def __init__(self):
        self.name = "Mutant Dog"
        self.hp = 20
        self.damage = 7

        self.xp = 15
        self.scrap = 5
        self.dodge = 0.8
