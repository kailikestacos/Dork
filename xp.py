from player import Player


class Perk:
    def __init__(self):
        raise NotImplementedError("Don't create raw perks!")

    def __str__(self):
        return self.name


class DanceFool(Perk):
    def __init__(self):
        self.name = "Dance Fool, Dance!"
        self.description = "Gain a bonus to dodging ranged attacks!"


class ImprovedBlocking(Perk):
    def __init__(self):
        self.name = "Improved Blocking"
        self.description = "Gain a bonus to dodging melee attacks!"


class PreciseAim(Perk):
    def __init__(self):
        self.name = "Precise Aim"
        self.description = "Damage with rifles is increased by 5% per rank!"

    def activate(self):
        for i in Player.inventory:
            if i.type is "rifle":
                added = i.damage * 0.05
                i.damage = i.damage + added