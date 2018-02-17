import items
import world
import random

class Player:
    def __init__(self):
        self.brawn = 0
        self.int = 0
        self.ath = 0
        self.cha = 0
        self.vital = 0
        self.dex = 0
        self.inventory = [items.Medkit(), items.PristinePlasmaSword()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100 + 5 * self.vital
        self.scrap = 10
        self.victory = False
        self.unarmed = 3 + 1 * self.brawn
        self.level = 1
        self.xp = 0
        self.xp_needed = 200

    def level_up(self):
        self.level = self. level + 1
        print("Level up! You are now level {}!".format(self.level))
        self.brawn = self.brawn +1
        self.int = self.int +1
        self.ath = self.ath +1
        self.cha = self.cha +1
        self.vital = self.vital+1
        self.dex = self.dex +1
        self.xp_needed = self.xp_needed + 100 * self.level

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item.name))
        print("Scrap: {}".format(self.scrap))

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any healing items!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose a healing item: ")
            print("{}. {}".format(i, item.name))
            valid = False
            while not valid:
                choice = input("")
                try:
                    to_eat = consumables[int(choice) -1]
                    self.hp = min(100, self.hp + to_eat.healing_value)
                    self.inventory.remove(to_eat)
                    print("Current HP is {}".format(self.hp))
                    valid = True
                except(ValueError, IndexError):
                    print("Your choice is not valid, pick again.")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        current_weapon = None
        weapons = []
        has_weapon = False
        for i in self.inventory:
            if i.type is "weapon":
                has_weapon = True
                weapons.append(i.name)

        weapons_str = ", "
        weapons_str = weapons_str.join(weapons)
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        if has_weapon is False:
            print("You strike the {} with a punch!".format(enemy.name))
            enemy.hp -= self.unarmed
        else:
            while current_weapon is None:
                player_input = input("What do you attack with?\n\n %s\n" % weapons_str)
                current_weapon = next((i for i in self.inventory if i.name == player_input), None)
                if current_weapon is None:
                    print("That's not a weapon, you dork. Try again.")
                r = random.random()
                if r < 0.7:
                    print("You strike the {} with {}!".format(enemy.name, current_weapon.name))
                    enemy.hp -= current_weapon.damage

                elif r < enemy.dodge:
                    print("The {} Dodges your attack!".format(enemy.name))
        if not enemy.is_alive():
            print("You have killed {}!".format(enemy.name))
            self.xp = self.xp + enemy.xp
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)



