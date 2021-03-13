from math import comb
from random import randint
from tables import load_pay_table
from utils import print_winnings
from utils import print_game_odds
from utils import odds
from utils import total_comb
from utils import pick
from utils import divide_chunks

def combo_2(played):
    # Playing ? number combo with groups of 2
    # we get the total number of combinations
    # multiplied by the winnings for each level
    # and add them together to get the total possible winning.
    # divide that my total combinations we get the average
    # amount won per game.
    
    # now because we are actually playing combo groups of 2
    # the winnings is based on that
    base_two_groups = comb(played, 2)
    total_combos = 0
    total_won = 0
    level_won = 0
    level_combos = 0

    for caught in range(played, -1, -1):
        level_combos = total_comb(played, caught)
        paid_two_groups = comb(caught, 2)
        # We need to divide the winnings by the base 2 groups
        # to get back to $1 spend per game.
        # Game index zero based
        level_won = level_combos * paid_two_groups * pay_table[1][2] / base_two_groups
        total_combos += level_combos
        total_won += level_won
        print('\nways to get ' + str(caught) + ' of ' + str(played) + ' ' + str(level_combos))
        print('number of 2 groups in ' + str(caught) + ' :' + str(paid_two_groups))
        print('winnings for ' + str(caught) + ' of ' + str(played) + ' ' + str(level_won))
 
    print('\ntotal combos   :' + str(total_combos))
    print('total winnings :' + str(total_won))
    average_return = total_won / total_combos
    print('combo_2 average returns:' + str(average_return))
    print()
