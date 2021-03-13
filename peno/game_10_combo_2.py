from math import comb
from random import randint
from tables import load_pay_table
from utils import print_winnings
from utils import print_game_odds
from utils import odds
from utils import total_comb
from utils import pick
from utils import divide_chunks

def game_10_combo_2(games):
    """
    This is a 10 number game using combos of 2
    """
    winnings = 0
    cost = 0

    for game in range(1,games+1):
        # >>> comb(10,2) 45
        cost+= 45
        played = pick(10)
        picked = pick(20)
        caught = 0;
        gamewon = 0;

        for play in played:
            if play in picked:
                caught+= 1

        two_groups = comb(caught, 2)
        if two_groups > 0:
            gamewon+= 12 * two_groups

        winnings+= gamewon

    print('--------------------------------------')
    print('total games played:' + str(games))
    print('total cost:' + str(cost))
    print('total winnings:' + str(winnings))
    print('total proffit:' + str(winnings - cost))
    print('pay ratio:' + str(winnings / cost))
