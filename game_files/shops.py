import datafuncs

def buyw1(person):
    print(f"You have {person.coins} coins.")
    if person.coins < 50:
        print("you're too broke to buy anything for now")
    else:
        choose = input(f'Upgrade health by 5: 50 coins, '
                       f'Upgrade damage multiplier by 0.1, 100 coins. '
                       f'Upgrade shield by 1: 100 coins.'
                       f'Type A for health upgrade and B for damage upgrade. C for shield upgrade. ')
        choose = choose.upper()
        if choose == 'A':
            person.coins -= 50
            person.health += 5
            print(f'Your health is now {person.health}!')
        elif choose == 'B':
            if person.coins >= 100:
                person.coins -= 100
                person.dmgmulti += 0.1
                person.dmgmulti = round(person.dmgmulti, 1)
                datafuncs.update_single_variable('gamedata.csv', person.name, 'dmgmulti', person.dmgmulti)
                print(f'Your damage multiplier is now {person.dmgmulti}!')
            else:
                print('not enough coins')
        elif choose == 'C':
            if person.coins >= 100:
                person.coins -= 100
                person.shield += 1
                print(f'Your shield now tanks {person.shield} damage!')
            else:
                print('not enough coins')
        else:
            print('You typed something wrong.')
    # datafuncs.gameupd(person)
    datafuncs.update_single_variable('gamedata.csv', person.name, 'coins', person.coins)
    choose = input("buy more? type Y to do so. ")
    if choose.upper() == 'Y':
        buyw1(person)

def buyw2(person):
    print(f"You have {person.coins} coins.")
    if person.coins < 225:
        print("you're too broke to buy anything for now")
    else:
        choose = input(f'Upgrade health by 25: 225 coins. '
                       f'Upgrade damage multiplier by 0.3, 250 coins. '
                       f'Upgrade shield by 3: 250 coins.'
                       f'Upgrade critical chance by 1% for 5000 coins.'
                       f'Upgrade critical damage multiplier by 0.5 for 1000 coins.'
                       f'Increase accuracy by 1% for 2500 coins.'
                       f'Type A for health upgrade and B for damage upgrade. C for shield upgrade.'
                       f'D for critical chance upgrade. E for critical damage upgrade.'
                       f'F for accuracy upgrade.')
        choose = choose.upper()
        if choose == 'A':
            person.coins -= 225
            person.health += 25
            print(f'Your health is now {person.health}!')
        elif choose == 'B':
            if person.coins >= 250:
                person.coins -= 250
                person.dmgmulti += 0.3
                person.dmgmulti = round(person.dmgmulti, 1)
                datafuncs.update_single_variable('gamedata.csv', person.name, 'dmgmulti', person.dmgmulti)
                print(f'Your damage multiplier is now {person.dmgmulti}!')
            else:
                print('not enough coins')
        elif choose == 'C':
            if person.coins >= 250:
                person.coins -= 250
                person.shield += 3
                print(f'Your shield now tanks {person.shield} damage!')
            else:
                print('not enough coins')
        elif choose == 'D':
            if person.critchance < 100:
                if person.coins >= 5000:
                    person.coins -= 5000
                    person.critchance += 1
                    print(f'Your critical chance is now {person.critchance}!')
                else:
                    print('not enough coins')
            else:
                print('You already have max critical chance!')
        elif choose == 'E':
            if person.coins >= 1000:
                person.coins -= 1000
                person.critmulti += 0.5
                person.critmulti = round(person.critmulti, 1)
                print(f'Your critical hits now do {person.critmulti} times damage!')
            else:
                print('not enough coins')
        elif choose == 'F':
            if person.accuracy < 100:
                if person.coins >= 2500:
                    person.coins -= 2500
                    person.accuracy += 1
                    print(f'Your accuracy is now {person.accuracy}!')
                else:
                    print('not enough coins')
            else:
                print('You already have max accuracy!')
        else:
            print('You typed something wrong.')
    datafuncs.update_single_variable('gamedata.csv', person.name, 'coins', person.coins)
    choose = input("buy more? type Y to do so. ")
    if choose == 'Y':
        buyw2(person)
