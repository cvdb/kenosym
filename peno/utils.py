from math import comb
from random import randint
from tables import load_pay_table

def print_winnings():
    for game in range(0,len(pay_table)):
        wintxt = ''
        for caught in range(0,len(pay_table[game])):
            if pay_table[game][caught] > 0:
                wintxt = wintxt + ', {}~{}'.format(caught, pay_table[game][caught])
        if wintxt:
            print('game:' + str(game+1) + wintxt)

def print_game_odds(played):
    for caught in range(played, -1, -1):
        print('played: ' + str(played) + ' caught: ' + str(caught) + ' odds: ' + str(round(odds(played, caught), 2)));


# This is specific to Keno where there is
# a total of 80 numbers and 20 are drawn per game
def odds(picked, caught):
    return total_comb(picked, caught) / comb(80, picked)

# get the total number of possible combination
def total_comb(picked, caught):
    if caught > picked:
        return 0
    else:
        return comb(20, caught) * comb(60, picked - caught)

# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

def pick(tot):
    # pick 20 random numbers from 1 to 80 inclusive
    # no duplicates allowed
    picked = []
    while len(picked) < tot:
        num = randint(1, 80)
        if num not in picked:
            picked.append(num)
    picked.sort()
    return picked
