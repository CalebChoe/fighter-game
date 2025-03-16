"""
This file has all the game functions.
"""
# import time
import random
import datafuncs
import pandas as pd
import sounds
import shops
import quests

class player:

    def __init__(self, coins, level, name):
        self.coins = coins
        self.level = level
        self.name = name
guy = player(0, 0, 'bob')

def login():
    ask = input("played before? Type Y or N: ")
    ask = ask.upper()
    if ask == "Y":
        user = input("whats your user id: ")
        if datafuncs.check_user_id('gamedata.csv', user):
            # Read the CSV file into a DataFrame
            df = pd.read_csv('gamedata.csv')
            # Check if the user ID exists in the DataFrame
            if user not in df['userid'].values:
                print(f'User ID {user} not found.')
                print('reload the game')
                quit()
            # Extract the row corresponding to the user ID
            player_data = df[df['userid'] == user].iloc[0]
            # Extract specific variables
            coins = player_data['coins']
            level = player_data['level']
            userid = player_data['userid']
            health = player_data['health']
            dmgmulti = player_data['dmgmulti']
            shield = player_data['shield']
            critchance = player_data['critchance']
            critmulti = player_data['critmulti']
            accuracy = player_data['accuracy']
            world = player_data['world']
            print(f'Player Data for {user}:')
            print(f'Coins: {coins}')
            print(f'Level: {level}')
            print(f'User Id: {userid}')
            return coins, level, userid, health, dmgmulti, shield, critchance, critmulti, accuracy, world

    else:
        user = input("put in your unique user id. if its taken you must rerun the code. ")
        if not datafuncs.check_user_id('gamedata.csv', user):
            # Read the CSV file into a DataFrame
            datafuncs.add_data('gamedata.csv', [{'userid': user, 'coins': 0, 'level': 0, 'health': 50, 'dmgmulti': 1,
                                                 'shield': 0, 'critchance': 3, 'critmulti': 3, 'accuracy': 70,
                                                 'world': 1}])
            return 0, 0, user, 50, 1, 0, 3, 3, 70, 1, 0
        else:
            print('user id taken')
            quit()

def fight(person, enemy, enemyhp, enemydmgmin, enemydmgmax, maximum, coingain, levelgain, extradesc='', tut=False, starthp=""):
    sounds.endlessplay('fightmusic.mp3', 0)
    input(f'{enemy} spawned!')
    print(extradesc)
    ehp = enemyhp
    php = person.health
    if starthp != "":
        php = person.health
    while ehp > 0:
        turn = True
        extravar = True
        atk = random.randint(1, maximum)
        choose = input(f'pick an integer between 1 and {maximum}: ')

        try:
            choose = int(choose)
        except ValueError:
            print("you lost your turn! invalid integer")
            turn = False
            extravar = False
        if extravar:
            if choose < 1 or choose > maximum:
                print("you lost your turn! invalid integer")
                turn = False
        enemydamage = random.randint(enemydmgmin, enemydmgmax)
        dmg = 0
        if turn:
            dmg = maximum - abs(choose - atk)
            print(dmg)
            print(choose, atk)
            acc = random.randint(1, 100)
            critical = random.randint(1, 100)
            if acc <= person.accuracy:
                if critical <= person.critchance:
                    ehp -= dmg * person.dmgmulti * person.critmulti
                    sounds.playsound('explode.mp3', 1)
                    print(f'Critical Hit!!!You dealt {dmg * person.dmgmulti * person.critmulti} damage!'
                          f'{enemy} now has {ehp} health.')
                else:
                    ehp -= dmg * person.dmgmulti
                    sounds.playsound('explode.mp3', 1)
                    print(f'You dealt {dmg * person.dmgmulti} damage! {enemy} now has {ehp} health.')
            else:
                print(f"You missed lol. 0 damage dealt. {enemy} now has {ehp} health.")
        if person.shield > enemydamage:
            print(f'Your shield is so high you took no damage. You now have {php} health.')
            php -= 0
        else:
            print(f'You took {enemydamage + person.shield} (-{person.shield} from shield) damage! You now have {php} health.')
            php -= enemydamage - person.shield
        if php <= 0:
            if tut:
                print('you found an easter egg! You somehow failed the tutorial.')
                print("we're gonna close the game. Try again if you wanna.")
                quit()
            print('You lost! +1 coin XD')
            person.coins += 1
            datafuncs.gameupd(person)
            return False
    sounds.stopsound(0)
    if ehp <= 0:
        input(f"battle won, {coingain} coins gained! {levelgain} levels gained!")
        person.coins += coingain
        person.level += levelgain
        datafuncs.gameupd(person)
    return php

def tutorial(person):
    print("press to continue")
    input("Welcome to the Monster Hunter game!")
    input("This is a very simple game.")
    input("There are monsters that can vary in strength based on what level you are.")
    input("Kill them to gain coins and level.")
    fight(person, 'zombie', 30, 1, 3, 10, 10, 1, tut=True)

def randomfight(person):
    datafuncs.gameupd(person)
    num = random.randint(1, 3)
    if person.world == 1:
        if num == 1:
            fight(person, 'zombie', 30, 3, 5, 10, 20, 1)
        elif num == 2:
            fight(person, 'tank zombie', 60, 3, 5, 10, 35, 2)
        elif num == 3:
            if person.level > 20:
                e = random.randint(1, 2)
                if e == 1:
                    fight(person, 'mega zombie', 150, 10, 15, 10, 60, 3)
                else:
                    fight(person, 'mega zombie: premium edition', 300, 20, 40, 20, 200, 5,
                          'this mega zombie can take up to double damage compared to other zombies, but it is very tanky.')
        if person.level >= 50:
            up = input("You've reached at least level 50, want to go to the next world?"
                       "There are tougher enemies with greater rewards. You can't come back to world 1."
                       "You will then gain the ability to increase your chance for a critical hit,"
                       "deal more damage with critical hits, and decrease your chance of missing an attack."
                       "There is also more in the shop."
                       "Type Y to go. ")
            if up.upper() == 'Y':
                print('Good luck.')
                person.world = 2
    elif person.world == 2:
        num = random.randint(1, 2)
        if num == 1:
            fight(person, 'evolved zombie', 300, 15, 30, 10, 100, 5)
        elif num == 2:
            fight(person, 'archer', 100, 50, 75, 10, 100, 5)

    contin = input('Quit playing? Y for yes. ')
    if contin.upper() == 'Y':
        print('closing..')
        quit()
    else:
        choose = input('Go to Shop? Type Y to do so. ')
        if choose.upper() == 'Y':
            if person.world == 1:
                shops.buyw1(person)
            elif person.world == 2:
                shops.buyw2(person)
    e = input('Type Y if you want to start a fight. ')
    if e.upper() == 'Y':
        print('starting fight...')
        randomfight(person)
    e = input('Type Y to do a challenging quest with lots of monsters. ')
    if e.upper() == 'Y':
        if player.storyquests == 0:
            if quests.quest1(player):
                player.storyquests += 1
        elif player.storyquests == 1:
            if quests.quest2(player):
                player.storyquests += 1
