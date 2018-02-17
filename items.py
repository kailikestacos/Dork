class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not initialize raw weapon. Please specify.")

    def __str__(self):
        return self.name


class SalvagedPlasmaPistol(Weapon):

    def __init__(self):
        self.description = "A small, makeshift handgun, pulse firing small, blue unstable blasts of plasma"
        self.value = 20
        self.damage = 5
        self.name = "Salvaged Plasma Pistol"
        self.type = "weapon"


class SalvagedPlasmaRifle(Weapon):
    def __init__(self):
        self.name = "Salvaged Plasma Rifle"
        self.description = """
        A scrapped up rifle, it looks like an ancient musket with heavy modification for firing unstable blasts of plasma
        """
        self.damage = 10
        self.value = 60
        self.type = "weapon"

class SalvagedPlasmaAxe(Weapon):

    def __init__(self):
        self.name = "Salvaged Plasma Axe"
        self.description = """
        Salvaged from Exterminator parts, the blue blade of unstable plasma protrudes from the handle.
        """
        self.value = 50
        self.name = "Salvaged Plasma Axe"
        self.damage = 10
        self.type = "weapon"


class SalvagedPlasmaSword(Weapon):
    def __init__(self):
        self.name = "Salvaged Plasma sword"
        self.description = "The scrappy hilt shouldn't fool one into thinking it's blue blade of plasma is fragile."
        self.damage = 20
        self.value = 75
        self.type = "weapon"


class PristinePlasmaPistol(Weapon):
    def __init__(self):
        self.damage = 8
        self.name = "Plasma Pistol"
        self.description = "A clean, new weapon, fires small blasts of blue plasma."
        self.value = 30
        self.type = "weapon"


class PristinePlasmaRifle(Weapon):
    def __init__(self):
        self.name = "Plasma Rifle"
        self.description = """
        A new, shiny rifle, fires out blasts of plasma.
        """
        self.damage = 15
        self.value = 70
        self.type = "weapon"


class PristinePlasmaAxe(Weapon):

    def __init__(self):
        self.value = 604
        self.name = "Plasma Axe"
        self.description = "A brand new axe with a blade of plasma, not to be reckoned with."
        self.damage = 15
        self.type = "weapon"


class PristinePlasmaSword(Weapon):
    def __init__(self):
        self.description = "A new sword, a blade of plasma protrudes from the hilt"
        self.value = 85
        self.name = "Plasma Sword"
        self.damage = 25
        self.type = "weapon"


class Ammo:
    def __init__(self):
        raise NotImplementedError("Do not initialize raw Ammo.")

    def __str__(self):
        return self.name


class EBattery(Ammo):
    def __init__(self):
        self.name = "E-Batt"
        self.description = """A modified Double A battery that serves as ammunition for plasma guns. It emits a faint blue glow.
        """
        self.value = 2
        self.type = "ammo"


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class MedkitLight(Consumable):
    def __init__(self):
        self.name = "Light Medkit"
        self.healing_value = 20
        self.value = 20
        self.type = "consumable"


class Medkit(Consumable):
    def __init__(self):
        self.name = "Medkit"
        self.healing_value = 35
        self.value = 50
        self.type = "consumable"


class MedkitHeavy(Consumable):
    def __init__(self):
        self.name = "Heavy Medkit"
        self.healing_value = 50
        self.value = 100
        self.type = "consumable"