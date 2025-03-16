# import csvdata
import datafuncs
# import pandas as pd
import game

class player:
    def __init__(self, coins, level, name, health, dmgmulti, shield, critchance, critmulti, accuracy, world, storytasks):
        self.coins = coins
        self.level = level
        self.name = name
        self.health = health
        self.dmgmulti = dmgmulti
        self.shield = shield
        self.critchance = critchance
        self.critmulti = critmulti
        self.accuracy = accuracy
        self.world = world
        self.storytasks = storytasks

guy = player(0, 0, 'bob', 50, 1.0, 0, 3, 3, 70, 1, False)

def main():
    print("Executed when run directly")

if __name__ == "__main__":
    # datafuncs.generate_dataframe('gamedata.csv', ['userid', 'coins', 'level', 'health', 'dmgmulti',
    #                                              'critchance', 'critmulti', 'accuracy', 'world'])
    print('run')
    guy.coins, guy.level, guy.name, guy.health, guy.dmgmulti, guy.shield, guy.critchance, guy.critmulti, \
        guy.accuracy, guy.world, guy.storytasks = game.login()
    if guy.level < 1:
        game.tutorial(guy)
    game.randomfight(guy)
    main()
