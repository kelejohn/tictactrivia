bonus1 = 0
bonus2 = 0

def bonus_move(player):
    global bonus1
    global bonus2
    if player == 1:
        bonus1+=1
    elif player==2:
        bonus2+=1


def player_bonus(player):
    global bonus1
    global bonus2
    if player == 1:
        return bonus1 > 0
    elif player == 2:
        return bonus2 > 0

def used(player):
    global bonus1
    global bonus2
    if player == 1:
        bonus1 -= 1
    elif player == 2:
        bonus2 -= 1