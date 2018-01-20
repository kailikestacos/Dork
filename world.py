import random
import enemy
import npc

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
 You find yourself in a cave with a flickering torch on the wall.
 You can make out four paths, each equally as dark and foreboding.
 """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemy.GiantSpider()
        elif r < 0.80:
            self.enemy = enemy.Ogre()
        elif r < 0.95:
            self.enemy = enemy.BatColony()
        else:
            self.enemy = enemy.Rockmonster()


        super().__init__(x, y)
    def intro_text(self):
        if self.enemy.is_alive:
            text = self.enemy.alive_text
        else:
            text = self.enemy.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("{} attacks for {} damage, leaving you at {} HP.".format(self.enemy.name, self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
 You see a bright light in the distance...
 ... it grows as you get closer! It's sunlight!


 Victory is yours!
 """


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            A boring part of the cave
            """

        else:
            return """
            You pick up some gold someone dropped
            """


world_dsl = """
|EN|EN|VT|EN|EN|
|EN|  |  |  |EN|
|EN|FG|EN|  |TT|
|TT|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


class TraderTile(MapTile):
    def __init(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['B','b']:
                print("Here's what you can buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S','s']:
                print("Here's what you can sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Do not keep testing me with invalid actions.")

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice, mortal fool!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def intro_text(self):
            return """
        Ayyy you see a dank trader
        """


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "TT": TraderTile,
                  "FG": FindGoldTile,
                  "  ": None}

