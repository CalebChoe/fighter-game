# from game import fight

def quest1(player):
    hp = player.health
    for i in range(5):
        score = fight(player, 'zombie', 30, 3, 5, 10, 20, 1)
        if not score:
            print('bro failed the task')
            return False
        hp = score
    for i in range(5):
        score = fight(player, 'tank zombie', 60, 3, 5, 10, 35, 2, starthp=hp)
        if not score:
            print('bro failed the task')
            return False
        hp = score
    for i in range(3):
        score = fight(player, 'mega zombie', 150, 10, 15, 10, 60, 3)
        if not score:
            print('bro failed the task')
            return False
        hp = score
    score = fight(player, 'mega zombie: premium edition', 300, 20, 40, 20, 200, 5,
                  'this mega zombie can take up to double damage compared to other zombies, but it is very tanky.')
    if not score:
        print('bro failed the task')
        return False
    return True

def quest2(player):
    for i in range(5):
        score = fight(player, 'mystery man', 1000, 50, 100, 10, 1000, 0)
        if not score:
            print('bro failed the task')
            return False
        hp = score
    player.level += 1
    return True
